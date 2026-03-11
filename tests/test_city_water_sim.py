from playwright.sync_api import sync_playwright
import os

def test_city_water_sim():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Path to the simulation file
        file_path = "file:///app/Simulations/EngineeringTechnologyScience/CityWaterInfrastructureSimulation.html"

        # Go to the local page
        page.goto(file_path)

        # Wait for initial load
        page.wait_for_timeout(1000)

        # 1. Close modal
        page.evaluate("document.getElementById('close-modal').click()")
        page.wait_for_timeout(500)

        # 2. Set constraints via evaluate to ensure no errors with range inputs
        page.evaluate("document.getElementById('max-budget').value = '400'; document.getElementById('max-budget').dispatchEvent(new Event('input'))")
        page.evaluate("document.getElementById('min-capacity').value = '450'; document.getElementById('min-capacity').dispatchEvent(new Event('input'))")
        page.evaluate("document.getElementById('max-env-impact').value = '75'; document.getElementById('max-env-impact').dispatchEvent(new Event('input'))")

        # Start game
        page.evaluate("document.getElementById('start-btn').click()")
        page.wait_for_timeout(500)

        # 3. Start some projects using the globally exposed function to bypass overlapping UI issues
        page.evaluate("window.startProject('repair')")
        page.evaluate("window.startProject('conservation')")

        # Advance 2 years
        page.evaluate("document.getElementById('advance-year-btn').click()")
        page.wait_for_timeout(200)
        page.evaluate("document.getElementById('advance-year-btn').click()")
        page.wait_for_timeout(1000) # Give chart time to animate

        # Take screenshot for verification
        os.makedirs('/home/jules/verification', exist_ok=True)
        screenshot_path = '/home/jules/verification/city_water_sim.png'
        page.screenshot(path=screenshot_path)

        # Verify values changed somewhat
        year = page.locator('#current-year-display').inner_text()
        assert year == "2027", f"Expected year 2027, got {year}"

        print(f"Test complete. Screenshot saved to {screenshot_path}")
        browser.close()

if __name__ == "__main__":
    test_city_water_sim()