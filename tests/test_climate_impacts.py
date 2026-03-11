import os
from playwright.sync_api import sync_playwright

def test_climate_impacts():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        base_dir = "/app"
        file_path = f"file://{os.path.join(base_dir, 'Simulations/EarthSpaceSciences/GlobalClimateImpacts.html')}"

        print(f"Navigating to {file_path}")
        page.goto(file_path, wait_until="networkidle")

        # 1. Verify UI Elements
        print("Verifying UI elements...")
        assert page.locator("h1", has_text="Global Climate Impacts & Mitigation Forecast").is_visible()
        assert page.locator("#co2Chart").is_visible()
        assert page.locator("#tempChart").is_visible()

        # 2. Check baseline forecast state (Business As Usual vs Mitigated should be identical initially)
        # Wait a moment for initial charts to render
        page.wait_for_timeout(500)

        initial_forecast = page.evaluate("window.simForecast")
        print(f"Initial forecast: {initial_forecast}")

        # In baseline state, mitigated == BAU
        assert abs(initial_forecast["finalMitTemp"] - initial_forecast["finalBauTemp"]) < 0.01, "Initially mitigated should equal BAU"

        # 3. Test Renewable Energy Toggle (Addresses HS-ESS3-4)
        print("Testing Renewable Energy mitigation...")
        page.locator("button[data-solution='renewable']").click()

        # Wait for chart animation
        page.wait_for_timeout(500)

        renew_forecast = page.evaluate("window.simForecast")
        print(f"Renewable forecast: {renew_forecast}")

        # Mitigated temp should be lower than BAU
        assert renew_forecast["finalMitTemp"] < renew_forecast["finalBauTemp"], "Renewables should reduce forecasted temperature"

        # Mitigated pH should be higher (less acidic) than BAU
        assert renew_forecast["finalMitPH"] > renew_forecast["finalBauPH"], "Renewables should reduce ocean acidification (higher pH)"

        # Turn off renewable
        page.locator("button[data-solution='renewable']").click()

        # 4. Test Geoengineering Toggle (Crucial scientific distinction)
        print("Testing Geoengineering mitigation...")
        page.locator("button[data-solution='geoeng']").click()

        page.wait_for_timeout(500)

        geo_forecast = page.evaluate("window.simForecast")
        print(f"Geoengineering forecast: {geo_forecast}")

        # Mitigated temp should be lower than BAU
        assert geo_forecast["finalMitTemp"] < geo_forecast["finalBauTemp"], "Geoengineering should reduce forecasted temperature"

        # BUT Mitigated pH should be IDENTICAL to BAU because geoeng doesn't remove CO2 from the atmosphere
        assert abs(geo_forecast["finalMitPH"] - geo_forecast["finalBauPH"]) < 0.01, "Geoengineering should NOT improve ocean acidification"

        print("All Climate Impact tests passed!")
        browser.close()

if __name__ == "__main__":
    test_climate_impacts()