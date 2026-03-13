import os
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture
def simulation_page(page: Page):
    # Construct the file path dynamically
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', 'Simulations', 'EarthSpaceSciences', 'EarthSystemsInteractions.html')

    # Block external requests to avoid timeouts in restricted environments
    page.route("**/*tailwindcss.com*", lambda route: route.abort())
    page.route("**/*chart.js*", lambda route: route.abort())

    page.goto(f"file://{file_path}")
    return page

def test_initial_render(simulation_page: Page):
    # Verify the page title and basic elements
    expect(simulation_page).to_have_title("Earth Systems Interactions Simulator")
    expect(simulation_page.locator("h1")).to_contain_text("Earth Systems Interactions Simulator")

    # Verify default control values
    expect(simulation_page.locator("#fossilVal")).to_have_text("10")
    expect(simulation_page.locator("#deforestVal")).to_have_text("1.5")

    # Verify initial dashboard displays
    expect(simulation_page.locator("#displayCO2")).to_contain_text("415 ppm")
    expect(simulation_page.locator("#displayPH")).to_contain_text("8.10")
    expect(simulation_page.locator("#displayBiomass")).to_contain_text("100")

def test_simulation_state_updates(simulation_page: Page):
    # Verify the exposed simulation state object
    state = simulation_page.evaluate("window.simulationState")
    assert state['year'] == 0
    assert state['co2_ppm'] == 415.0

    # Run simulation for a few steps
    simulation_page.evaluate("window.runSimulationInstant(10)")

    new_state = simulation_page.evaluate("window.simulationState")
    assert new_state['year'] == 10

    # Check that CO2 increased under default emission parameters
    assert new_state['co2_ppm'] > 415.0

    # Check that Ocean pH decreased (acidification) due to higher CO2
    assert new_state['ocean_pH'] < 8.10

def test_slider_inputs_affect_model(simulation_page: Page):
    # Increase emissions significantly
    simulation_page.fill("#fossilEmissions", "30")
    simulation_page.evaluate("document.getElementById('fossilEmissions').dispatchEvent(new Event('input'))")

    simulation_page.evaluate("window.runSimulationInstant(50)")

    state_high_emissions = simulation_page.evaluate("window.simulationState")

    # Reset and run with zero emissions
    simulation_page.evaluate("window.resetSimulation()")

    simulation_page.fill("#fossilEmissions", "0")
    simulation_page.evaluate("document.getElementById('fossilEmissions').dispatchEvent(new Event('input'))")

    simulation_page.evaluate("window.runSimulationInstant(50)")

    state_zero_emissions = simulation_page.evaluate("window.simulationState")

    # Verify higher emissions lead to higher atmospheric CO2
    assert state_high_emissions['co2_ppm'] > state_zero_emissions['co2_ppm']

    # Verify higher emissions lead to lower ocean pH
    assert state_high_emissions['ocean_pH'] < state_zero_emissions['ocean_pH']
