import os
from playwright.sync_api import sync_playwright

def test_resource_management():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        base_dir = "/app"
        file_path = f"file://{os.path.join(base_dir, 'Simulations/EarthSpaceSciences/ResourceManagementSimulator.html')}"

        print(f"Navigating to {file_path}")
        page.goto(file_path, wait_until="networkidle")

        # Set document to visible to ensure requestAnimationFrame fires
        page.evaluate("document.hidden = false;")

        # 1. Verify UI Elements
        print("Verifying UI elements...")
        assert page.locator("h1", has_text="Sustainable Resource Management Simulator").is_visible()
        assert page.locator("#simChart").is_visible()

        # 2. Verify Initial State
        initial_pop = page.locator("#popVal").inner_text()
        assert initial_pop == "10.0", f"Initial pop should be 10.0, got {initial_pop}"

        initial_bio = page.locator("#bioVal").inner_text()
        assert initial_bio == "100.0%", f"Initial biodiversity should be 100.0%, got {initial_bio}"

        # 3. Start Sim with default Intensive/Coal setup (high growth, high pollution/bio loss)
        print("Running default simulation (Coal + Intensive Ag)...")
        page.locator("#playBtn").click() # Start time

        # Run for ~2 seconds (representing ~2 years)
        page.wait_for_timeout(2000)

        page.locator("#playBtn").click() # Pause time

        post_default_state = page.evaluate("window.simState")
        print(f"State after default run: {post_default_state}")

        # Population should have grown (food and energy are sufficient)
        assert post_default_state["population"] > 10.0, "Population should grow with intensive resources"

        # Biodiversity should have dropped
        assert post_default_state["biodiversity"] < 100.0, "Biodiversity should drop with coal and intensive agriculture"

        # Pollution should have risen
        assert post_default_state["pollution"] > 0.0, "Pollution should rise with coal and intensive agriculture"

        # 4. Test Policy Change to Conservation/Renewable
        print("Testing policy switch to Renewable + Conservation...")
        page.locator("#btn-renew").click()
        page.locator("#btn-conserve").click()

        page.locator("#playBtn").click() # Resume time
        page.wait_for_timeout(2000)
        page.locator("#playBtn").click() # Pause

        post_green_state = page.evaluate("window.simState")
        print(f"State after green run: {post_green_state}")

        # Pollution should be dropping or stable, definitely lower rate than before
        assert post_green_state["pollution"] < post_default_state["pollution"] or post_green_state["pollution"] == 0, "Pollution should decrease with renewables"

        # But because conservation only yields 6 food, and population is > 10, they should be starving
        assert post_green_state["starving"] == True, "Population should be starving because demand > supply"

        # And population should have decreased from starvation
        assert post_green_state["population"] < post_default_state["population"], "Population should decrease due to starvation"

        # 5. Test Reset
        page.locator("#resetBtn").click()
        reset_pop = page.locator("#popVal").inner_text()
        assert reset_pop == "10.0", "Population should reset to 10.0"

        print("All Resource Management tests passed!")
        browser.close()

if __name__ == "__main__":
    test_resource_management()