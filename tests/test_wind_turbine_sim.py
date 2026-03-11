from playwright.sync_api import sync_playwright
import os

def test_wind_turbine_sim():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_path = "file://" + os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'EngineeringTechnologyScience', 'WindTurbineSimulation.html'))
        page.goto(file_path)
        page.wait_for_timeout(1000)

        # 1. Update inputs
        page.evaluate("document.getElementById('wind-speed').value = '15'; document.getElementById('wind-speed').dispatchEvent(new Event('input'))")
        page.evaluate("document.getElementById('blade-length').value = '80'; document.getElementById('blade-length').dispatchEvent(new Event('input'))")
        page.wait_for_timeout(500)

        # 2. Record trial
        page.evaluate("document.getElementById('record-data').click()")
        page.wait_for_timeout(500)

        # Verify
        power = page.locator('#power-output').inner_text()
        print(f"Recorded Power: {power}")
        assert power is not None and power != "0.0", "Power should be calculated and present."

        print(f"Test complete.")
        browser.close()

if __name__ == "__main__":
    test_wind_turbine_sim()
