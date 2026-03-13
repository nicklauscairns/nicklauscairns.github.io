import os
import pytest
from playwright.sync_api import Page, expect

def test_hs_ess3_2_energy_simulation(page: Page):
    # Construct the file path relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = "file://" + os.path.join(current_dir, "..", "Simulations", "EarthSpaceSciences", "EnergyResourcesCostBenefit.html")

    # Block external resources to prevent timeouts
    page.route("**/*tailwindcss.com*", lambda route: route.abort())
    page.route("**/*chart.js*", lambda route: route.abort())

    # Navigate to the simulation
    page.goto(file_path)

    # Allow simulation to initialize
    page.wait_for_timeout(1000)

    # Verify initial state metrics
    metrics_a = page.evaluate("window.currentMetricsA")
    assert metrics_a["energyProduced"] == 100  # 100 * 1.0 reliability for coal
    assert metrics_a["mineralsProduced"] == 100 # 100 + 0

    # Interact with Solution A: Change Energy Source to Nuclear and Scale
    page.select_option("#a-energy-type", "nuclear")
    page.fill("#a-energy-scale", "120")
    page.evaluate("document.getElementById('a-energy-scale').dispatchEvent(new Event('input'))")

    page.wait_for_timeout(500)

    # Verify updated state metrics
    new_metrics_a = page.evaluate("window.currentMetricsA")
    assert new_metrics_a["energyProduced"] == 120 # 120 * 1.0 reliability for nuclear
    assert new_metrics_a["ecoCost"] != metrics_a["ecoCost"]

    # Interact with Mitigation
    page.fill("#a-mitigation", "100")
    page.evaluate("document.getElementById('a-mitigation').dispatchEvent(new Event('input'))")

    page.wait_for_timeout(500)

    mitigated_metrics_a = page.evaluate("window.currentMetricsA")
    assert mitigated_metrics_a["envImpact"] < new_metrics_a["envImpact"]
    assert mitigated_metrics_a["socialRisk"] < new_metrics_a["socialRisk"]

    # Interact with Evaluation Section
    assert page.locator("#eval-success").is_hidden()

    page.check("input[name='preferred-solution'][value='B']")
    page.fill("#eval-evidence", "Solution B is better because it uses renewable solar energy and underground mining which meets the targets with lower long term impacts.")
    page.fill("#eval-strengths", "While Solution B has a higher initial economic cost, its environmental impact is significantly lower than Solution A.")
    page.fill("#eval-argument", "Therefore, based on the need to balance societal energy demands with environmental constraints, Solution B provides the best cost-benefit ratio.")

    # Trigger the evaluation check
    page.evaluate("window.checkEvaluation()")

    # Verify success message is visible
    expect(page.locator("#eval-success")).to_be_visible()
