import pytest
from playwright.sync_api import Page, expect
import os

def test_puertorico_gravity_anomaly_renders(page: Page):
    file_path = f"file://{os.path.abspath('Simulations/EarthSpaceSciences/PuertoRicoTrenchGravityAnomaly.html')}"
    page.goto(file_path)

    # Check title
    expect(page).to_have_title("Puerto Rico Trench Gravity Anomaly - NGSS HS-ESS2-1")

    # Check if canvas elements exist
    expect(page.locator('#threejs-container canvas')).to_be_visible()
    expect(page.locator('#gravityChart')).to_be_visible()

def test_puertorico_gravity_anomaly_controls(page: Page):
    file_path = f"file://{os.path.abspath('Simulations/EarthSpaceSciences/PuertoRicoTrenchGravityAnomaly.html')}"
    page.goto(file_path)

    # Verify initial state via window object
    state = page.evaluate("window.simulationState")
    assert state['angle'] == 45
    assert float(state['crustDensity']) == 2.9
    assert float(state['mantleDensity']) == 3.3
    assert float(state['trenchDepth']) == 8.4
    assert state['carbonatePlatform'] is False
    assert state['crustalThinning'] is False

    # Change Subduction Angle
    page.evaluate("document.getElementById('angleSlider').value = 60")
    page.evaluate("document.getElementById('angleSlider').dispatchEvent(new Event('input'))")

    # Change Trench Depth
    page.evaluate("document.getElementById('trenchDepthSlider').value = 9.5")
    page.evaluate("document.getElementById('trenchDepthSlider').dispatchEvent(new Event('input'))")

    # Toggle Mystery Variables
    page.check("#mysteryMassToggle")
    page.evaluate("document.getElementById('mysteryMassToggle').dispatchEvent(new Event('change'))")

    page.check("#crustalThinningToggle")
    page.evaluate("document.getElementById('crustalThinningToggle').dispatchEvent(new Event('change'))")

    # Verify state updated
    expect(page.locator('#angleValue')).to_have_text('60°')
    expect(page.locator('#trenchDepthValue')).to_have_text('9.5 km')

    new_state = page.evaluate("window.simulationState")
    assert new_state['angle'] == 60
    assert float(new_state['trenchDepth']) == 9.5
    assert new_state['carbonatePlatform'] is True
    assert new_state['crustalThinning'] is True

    # Check if the calculated minimum anomaly updated (it should be displayed)
    min_anomaly_text = page.locator('#minAnomalyDisplay').inner_text()
    assert "mGal" in min_anomaly_text

def test_puertorico_gravity_anomaly_reset(page: Page):
    file_path = f"file://{os.path.abspath('Simulations/EarthSpaceSciences/PuertoRicoTrenchGravityAnomaly.html')}"
    page.goto(file_path)

    # Change some states
    page.evaluate("document.getElementById('angleSlider').value = 30")
    page.evaluate("document.getElementById('angleSlider').dispatchEvent(new Event('input'))")
    page.check("#mysteryMassToggle")
    page.evaluate("document.getElementById('mysteryMassToggle').dispatchEvent(new Event('change'))")

    expect(page.locator('#angleValue')).to_have_text('30°')

    # Click reset
    page.click("#resetBtn")

    expect(page.locator('#angleValue')).to_have_text('45°')

    # Verify reset to initial state
    reset_state = page.evaluate("window.simulationState")
    assert reset_state['angle'] == 45
    assert reset_state['carbonatePlatform'] is False
