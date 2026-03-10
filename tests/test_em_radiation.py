import os
from playwright.sync_api import sync_playwright

def test_em_radiation():
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'PhysicalSciences', 'EMRadiationEffects.html'))
    if not os.path.exists(html_path):
        html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'PhysicalScience', 'EMRadiationEffects.html'))

    file_uri = f"file://{html_path}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(file_uri, wait_until='networkidle')

        # Allow rendering
        page.evaluate("document.hidden = false;")
        page.wait_for_timeout(500)

        # 1. Test Initial State (IR - Thermal)
        band = page.evaluate("window.testingTools.getBand()")
        assert band['name'] == "Infrared (IR)", f"Expected IR initially, got {band['name']}"
        assert band['type'] == "thermal"

        initial_temp = page.evaluate("window.testingTools.getTemp()")
        initial_dmg = page.evaluate("window.testingTools.getDamage()")

        # Wait for thermal effect
        page.wait_for_timeout(2000)

        heated_temp = page.evaluate("window.testingTools.getTemp()")
        heated_dmg = page.evaluate("window.testingTools.getDamage()")

        # Should heat up, but not damage
        assert heated_temp > initial_temp + 5, f"Expected temp to increase via IR, initial {initial_temp}, got {heated_temp}"
        assert heated_dmg == 0, f"Expected 0 damage via IR, got {heated_dmg}"

        # 2. Test Ionizing Radiation (Gamma Rays)
        page.evaluate("document.getElementById('em-slider').value = 7;")
        page.evaluate("document.getElementById('em-slider').dispatchEvent(new Event('input'))")

        # Verify it reset on switch IMMEDIATELY before particles spawn
        gamma_initial_dmg = page.evaluate("window.testingTools.getDamage()")
        assert gamma_initial_dmg == 0, f"Damage should reset to 0 on switch, got {gamma_initial_dmg}"

        page.wait_for_timeout(500)

        gamma_band = page.evaluate("window.testingTools.getBand()")
        assert gamma_band['name'] == "Gamma Rays", f"Expected Gamma Rays, got {gamma_band['name']}"
        assert gamma_band['type'] == "ionizing"

        # Wait for ionizing damage
        page.wait_for_timeout(2000)

        gamma_heated_temp = page.evaluate("window.testingTools.getTemp()")
        gamma_dmg = page.evaluate("window.testingTools.getDamage()")

        # Should damage significantly, but not heat directly
        assert gamma_dmg > 20, f"Expected significant ionizing damage (>20), got {gamma_dmg}"
        assert gamma_heated_temp <= 37.1, f"Gamma should not directly heat, got {gamma_heated_temp}"

        browser.close()

if __name__ == "__main__":
    test_em_radiation()
    print("All tests passed for EM Radiation Effects.")