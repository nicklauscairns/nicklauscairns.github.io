import os
from playwright.sync_api import sync_playwright

def test_ice_albedo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        base_dir = "/app"
        file_path = f"file://{os.path.join(base_dir, 'Simulations/EarthSpaceSciences/IceAlbedoFeedback.html')}"

        print(f"Navigating to {file_path}")
        page.goto(file_path, wait_until="networkidle")

        # Set document to visible to ensure requestAnimationFrame fires
        page.evaluate("document.hidden = false;")

        # 1. Verify UI Elements
        print("Verifying UI elements...")
        assert page.locator("h1", has_text="Ice-Albedo Feedback Loop").is_visible()
        assert page.locator("#earthView").is_visible()
        assert page.locator("#feedbackChart").is_visible()

        # 2. Verify Initial State
        initial_temp = page.locator("#tempDisplay").inner_text()
        assert initial_temp == "14.0°C", f"Initial temp should be 14.0°C, got {initial_temp}"

        initial_albedo = page.locator("#albedoDisplay").inner_text()
        assert float(initial_albedo) > 0.25, f"Initial albedo should be > 0.25, got {initial_albedo}"

        # 3. Increase GHG Forcing and Start Sim
        # Move slider to max using evaluate since Playwright fill on range inputs is flaky
        page.evaluate("document.getElementById('ghgInput').value = '2.0'")
        page.evaluate("document.getElementById('ghgInput').dispatchEvent(new Event('input'))")

        # Verify text updated
        assert "High" in page.locator("#ghgVal").inner_text()

        # Simulation should have auto-started from the input event
        page.wait_for_timeout(1000) # wait for ~60 frames

        # Pause sim
        page.locator("#toggleBtn").click()

        # 4. Verify Positive Feedback Occurred
        post_sim_state = page.evaluate("window.simState")

        print(f"State after running: Temp {post_sim_state['temp']}, Ice {post_sim_state['iceCoverage']}, Albedo {post_sim_state['albedo']}")

        # Temp should have increased
        assert post_sim_state["temp"] > 14.0, "Global temp should have risen due to GHG forcing"

        # Ice should have melted
        assert post_sim_state["iceCoverage"] < 25.0, "Ice coverage should have decreased due to warming"

        # Albedo should have dropped (less reflective ice)
        assert post_sim_state["albedo"] < float(initial_albedo), "Albedo should have decreased as ice melted"

        # 5. Test Reset
        page.locator("#resetBtn").click()

        reset_temp = page.locator("#tempDisplay").inner_text()
        assert reset_temp == "14.0°C", "Temp should reset to 14.0°C"

        print("All Ice-Albedo tests passed!")
        browser.close()

if __name__ == "__main__":
    test_ice_albedo()