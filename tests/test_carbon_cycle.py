import os
from playwright.sync_api import sync_playwright

def test_carbon_cycle():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Support both the physical science and life science filepaths
        current_dir = os.path.dirname(os.path.abspath(__file__))
        possible_paths = [
            os.path.join(current_dir, '..', 'Simulations', 'EarthSpaceSciences', 'GlobalCarbonCycleModel.html'),
            os.path.join(current_dir, '..', 'Simulations', 'LifeSciences', 'CarbonCycle.html')
        ]

        file_path = None
        for path in possible_paths:
            if os.path.exists(path):
                file_path = path
                break

        if not file_path:
            raise FileNotFoundError("Could not find GlobalCarbonCycleModel.html or CarbonCycle.html")

        print(f"Navigating to file://{file_path}")
        page.goto(f"file://{file_path}", wait_until="networkidle")

        # Set document to visible to ensure requestAnimationFrame fires
        page.evaluate("Object.defineProperty(document, 'hidden', { value: false, writable: false });")

        # 1. Verify UI Elements
        print("Verifying UI elements...")
        assert page.locator("h1").is_visible()

        if "GlobalCarbonCycleModel" in file_path:
            # 2. Verify Initial State and Conservation of Mass
            initial_mass = page.locator("#totalMass").inner_text()
            assert initial_mass == "44800", f"Initial total mass should be 44800, got {initial_mass}"

            initial_atmo = page.locator("#val-atmosphere").text_content()
            assert initial_atmo == "800", "Initial atmosphere should be 800"

            # 3. Increase Human Emissions and Start Sim
            print("Increasing emissions and running simulation...")
            page.evaluate("document.getElementById('humanFluxSlider').value = '30.0'")
            page.evaluate("document.getElementById('humanFluxSlider').dispatchEvent(new Event('input'))")

            page.locator("#toggleBtn").click() # Play time

            # Wait for simulation to run for a few seconds (frames)
            page.wait_for_timeout(2000)

            page.locator("#toggleBtn").click() # Pause time

            # 4. Verify State Changes
            post_sim_state = page.evaluate("window.simState")
            print(f"State after running: {post_sim_state}")

            # Atmosphere should have increased significantly due to max human flux
            assert post_sim_state["atmosphere"] > 800, "Atmosphere carbon should increase when human emissions are high"

            # Geosphere should have decreased
            assert post_sim_state["geosphere"] < 4000, "Geosphere carbon should decrease as fossil fuels are burned"

            # 5. Verify Conservation of Mass Holds
            current_total = post_sim_state["atmosphere"] + post_sim_state["biosphere"] + post_sim_state["hydrosphere"] + post_sim_state["geosphere"]
            assert abs(current_total - 44800) < 0.1, f"Conservation of mass violated. Total is {current_total}, expected 44800"

            # 6. Test Reset
            page.locator("#resetBtn").click()
            reset_atmo = page.locator("#val-atmosphere").text_content()
            assert reset_atmo == "800", "Atmosphere should reset to 800"

        else:
            # LifeSciences/CarbonCycle.html test path
            assert page.locator("#sim-year").text_content() == "2024"
            assert "800" in page.locator("#val-atm").text_content()
            page.locator("#btn-play").click()
            page.wait_for_timeout(3500)
            page.locator("#btn-play").click()
            year_text = page.locator("#sim-year").text_content()
            assert int(year_text) > 2024
            atm_text = page.locator("#val-atm").text_content().replace(' GT', '').replace(',', '')
            assert int(atm_text) > 800

        print("All Carbon Cycle tests passed!")
        browser.close()

if __name__ == "__main__":
    test_carbon_cycle()
