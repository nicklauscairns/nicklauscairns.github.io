feature/dna-protein-simulation-7135301846743549917
from playwright.sync_api import sync_playwright
import os

def test_carbon_cycle():
    possible_paths = [
        "Simulations/LifeSciences/CarbonCycle.html",
        "../Simulations/LifeSciences/CarbonCycle.html",
        "/app/Simulations/LifeSciences/CarbonCycle.html"
    ]

    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = os.path.abspath(path)
            break

    if not file_path:
        raise FileNotFoundError("Could not find CarbonCycle.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{file_path}", wait_until="networkidle")

        # 1. Verify Initial State (Year 2024, Atm = 800)
        assert page.locator("#sim-year").text_content() == "2024"
        assert "800" in page.locator("#val-atm").text_content()

        # 2. Start Simulation with defaults (10 GT emissions, 0 Bio balance)
        page.locator("#btn-play").click()

        # Wait a few ticks (3 seconds)
        page.wait_for_timeout(3500)

        # Pause
        page.locator("#btn-play").click()

        # Year should advance
        year_text = page.locator("#sim-year").text_content()
        assert int(year_text) > 2024

        # Atmosphere should have increased due to emissions (and ocean uptake mitigating it slightly)
        atm_text = page.locator("#val-atm").text_content().replace(' GT', '').replace(',', '')
        assert int(atm_text) > 800

        # Geosphere should have decreased
        geo_text = page.locator("#val-geo").text_content().replace(' GT', '').replace(',', '')
        assert int(geo_text) < 4000

        # 3. Test biological balance (Negative = more respiration = +Atm)
        page.evaluate("document.getElementById('flux-bio').value = '-5'; window.updateSimulation();")

        # Unpause for 2 ticks
        page.locator("#btn-play").click()
        page.wait_for_timeout(2500)
        page.locator("#btn-play").click()

        # Bio should be lower now
        bio_text = page.locator("#val-bio").text_content().replace(' GT', '').replace(',', '')
        assert int(bio_text) < 2000

        # Reset
        page.locator("#btn-reset").click()
        assert page.locator("#sim-year").text_content() == "2024"
        assert "800" in page.locator("#val-atm").text_content()

        # Take screenshot for verification
        os.makedirs('/home/jules/verification', exist_ok=True)
        page.screenshot(path='/home/jules/verification/carbon_cycle_screenshot.png', full_page=True)

        browser.close()
        print("Carbon Cycle simulation test passed.")
=======
import os
from playwright.sync_api import sync_playwright

def test_carbon_cycle():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        base_dir = "/app"
        file_path = f"file://{os.path.join(base_dir, 'Simulations/EarthSpaceSciences/GlobalCarbonCycleModel.html')}"

        print(f"Navigating to {file_path}")
        page.goto(file_path, wait_until="networkidle")

        # Set document to visible to ensure requestAnimationFrame fires
        page.evaluate("document.hidden = false;")

        # 1. Verify UI Elements
        print("Verifying UI elements...")
        assert page.locator("h1", has_text="Global Carbon Cycle Model").is_visible()
        assert page.locator("#svgDiagram").is_visible()
        assert page.locator("#carbonChart").is_visible()

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
        # Total mass should still be exactly 44800
        current_total = post_sim_state["atmosphere"] + post_sim_state["biosphere"] + post_sim_state["hydrosphere"] + post_sim_state["geosphere"]
        # Allow for tiny floating point rounding errors, but mathematically it should be precise
        assert abs(current_total - 44800) < 0.1, f"Conservation of mass violated. Total is {current_total}, expected 44800"

        ui_total = page.locator("#totalMass").inner_text()
        assert ui_total == "44800", "UI Total Mass text should remain 44800"

        # 6. Test Reset
        page.locator("#resetBtn").click()
        reset_atmo = page.locator("#val-atmosphere").text_content()
        assert reset_atmo == "800", "Atmosphere should reset to 800"

        print("All Carbon Cycle tests passed!")
        browser.close()
main

if __name__ == "__main__":
    test_carbon_cycle()