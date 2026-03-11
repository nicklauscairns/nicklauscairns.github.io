from playwright.sync_api import sync_playwright
import os

def test_ev_sim():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_path = "file://" + os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'EngineeringTechnologyScience', 'ElectricVehicleSimulation.html'))
        page.goto(file_path)
        page.wait_for_timeout(1000)

        # 1. Update inputs
        page.evaluate("document.getElementById('battery-capacity').value = '100'; document.getElementById('battery-capacity').dispatchEvent(new Event('input'))")
        page.wait_for_timeout(500)

        # 2. Record trial
        page.evaluate("document.getElementById('btn-record').click()")
        page.wait_for_timeout(500)

        # Verify
        range_val = page.locator('#out-range').inner_text()
        print(f"New Range with 100kWh: {range_val} km")
        assert range_val is not None and range_val != "0", "Range should be calculated and present."

        print(f"Test complete.")
        browser.close()

if __name__ == "__main__":
    test_ev_sim()
