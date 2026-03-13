import pytest
from playwright.sync_api import Page
import os
import time

def test_hs_ess3_4_simulation(page: Page):
    # Construct the path to the HTML file
    current_dir = os.path.dirname(__file__)
    file_path = os.path.abspath(os.path.join(current_dir, '..', 'Simulations', 'EarthSpaceSciences', 'TechnologicalSolutionEvaluation.html'))
    file_uri = f'file://{file_path}'

    # Intercept network requests for external resources to speed up tests and avoid timeouts
    page.route("**/*tailwindcss.com*", lambda route: route.abort())
    page.route("**/*chart.js*", lambda route: route.abort())

    # Mock Chart.js to prevent undefined errors when script is aborted
    page.add_init_script("""
        window.Chart = class {
            constructor(ctx, config) {
                this.ctx = ctx;
                this.config = config;
                this.data = config.data;
            }
            update() {}
        };
    """)

    page.goto(file_uri)

    # Check title
    assert "Urban Watershed Mitigation" in page.title()

    # Assert initial states
    budget_value = page.locator('#budget-value')
    assert budget_value.inner_text() == '10.0'

    run_btn = page.locator('#run-btn')
    assert run_btn.is_enabled()

    # Interact with sliders
    wetlands_slider = page.locator('#wetlands')
    wetlands_slider.evaluate("el => el.value = 2")
    wetlands_slider.evaluate("el => el.dispatchEvent(new Event('input'))")

    filtration_slider = page.locator('#filtration')
    filtration_slider.evaluate("el => el.value = 3")
    filtration_slider.evaluate("el => el.dispatchEvent(new Event('input'))")

    # Let the simulation update UI logic
    page.evaluate("window.updateSimulation()")

    # Check that cost has decreased the remaining budget
    # wetlands=2 * 1.5 = 3.0, filtration=3 * 2.5 = 7.5. Total = 10.5 > 10.0
    budget_warning = page.locator('#budget-warning')
    assert 'budget' in budget_warning.inner_text().lower()
    assert not run_btn.is_enabled() # Button should be disabled because we exceeded budget

    # Reduce filtration to be within budget
    filtration_slider.evaluate("el => el.value = 1")
    filtration_slider.evaluate("el => el.dispatchEvent(new Event('input'))")
    page.evaluate("window.updateSimulation()")

    # Run the simulation
    assert run_btn.is_enabled()
    page.evaluate("runSimulation()")

    # Wait for the 10 year loop to finish (10 * 200ms = 2s)
    page.wait_for_timeout(2500)

    # Assert run button text changed
    assert "Simulation Complete" in run_btn.inner_text()

    # Assert that metrics changed from their starting state (poll=100%, biod=40)
    # With filtration and wetlands, pollution should drop from 100%
    pollution_metric = page.locator('#metric-pollution')
    pollution_text = pollution_metric.inner_text().replace('%', '')
    pollution_val = float(pollution_text)

    assert pollution_val < 100.0, f"Expected pollution to decrease, but it was {pollution_val}"

    # Assert biodiversity went up
    biodiv_metric = page.locator('#metric-biodiversity')
    biodiv_text = biodiv_metric.inner_text().split('/')[0]
    biodiv_val = float(biodiv_text)

    assert biodiv_val > 40.0, f"Expected biodiversity to increase, but it was {biodiv_val}"

    # Reset simulation
    reset_btn = page.locator('#reset-btn')
    reset_btn.click()

    # Assert values reset
    assert budget_value.inner_text() == '10.0'
