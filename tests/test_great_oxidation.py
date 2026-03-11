import os
from playwright.sync_api import sync_playwright

def test_great_oxidation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        base_dir = "/app"
        file_path = f"file://{os.path.join(base_dir, 'Simulations/EarthSpaceSciences/GreatOxidationEvent.html')}"

        print(f"Navigating to {file_path}")
        page.goto(file_path, wait_until="networkidle")

        # Set document to visible to ensure requestAnimationFrame fires
        page.evaluate("document.hidden = false;")

        # 1. Verify UI Elements
        print("Verifying UI elements...")
        assert page.locator("h1", has_text="Coevolution of Earth & Life").is_visible()
        assert page.locator("#simView").is_visible()
        assert page.locator("#historyChart").is_visible()

        # 2. Verify Initial State
        initial_iron = page.locator("#ironVal").inner_text()
        assert "100" in initial_iron, f"Initial iron should be 100%, got {initial_iron}"

        initial_o2 = page.locator("#o2Val").inner_text()
        assert initial_o2 == "0.0%", "Initial O2 should be 0.0%"

        initial_time = page.locator("#timeDisplay").inner_text()
        assert initial_time == "2.50", "Initial time should be 2.50"

        # 3. Add Bacteria and Start Sim
        print("Adding bacteria and running simulation...")
        page.evaluate("document.getElementById('popSlider').value = '50'")
        page.evaluate("document.getElementById('popSlider').dispatchEvent(new Event('input'))")

        page.locator("#toggleBtn").click() # Start time

        # Wait for simulation to run long enough to deplete iron sink and build O2
        # This will require a bit of real time since dt is tied to time scaling.
        page.wait_for_timeout(3000)

        page.locator("#toggleBtn").click() # Pause time

        # 4. Verify State Changes
        post_sim_state = page.evaluate("window.simState")
        print(f"State after running: {post_sim_state}")

        # Iron sink should be completely depleted
        assert post_sim_state["dissolvedIron"] < 100.0, "Iron sink should be depleted by oxygen"

        # Time should have decreased (moved closer to present)
        assert post_sim_state["time"] < 2.50, "Time should have advanced"

        print("All Great Oxidation tests passed!")
        browser.close()

if __name__ == "__main__":
    test_great_oxidation()