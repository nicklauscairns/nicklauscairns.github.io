import os
from playwright.sync_api import sync_playwright

def test_human_settlement():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        base_dir = "/app"
        file_path = f"file://{os.path.join(base_dir, 'Simulations/EarthSpaceSciences/HumanMigrationSettlementSimulator.html')}"

        print(f"Navigating to {file_path}")
        page.goto(file_path, wait_until="networkidle")

        # Set document to visible to ensure requestAnimationFrame fires
        page.evaluate("document.hidden = false;")

        # 1. Verify UI Elements
        print("Verifying UI elements...")
        assert page.locator("h1", has_text="Human Settlement & Migration Simulator").is_visible()
        assert page.locator("#mapCanvas").is_visible()

        # 2. Verify Initial State
        initial_pop = page.locator("#popDisplay").inner_text()
        assert int(initial_pop) == 50, f"Initial population should be 50, got {initial_pop}"

        initial_year = page.locator("#yearDisplay").inner_text()
        assert initial_year == "0", "Initial year should be 0"

        # 3. Start Sim and allow agents to settle
        print("Running simulation to allow settlement...")
        page.locator("#toggleBtn").click() # Start Sim
        page.wait_for_timeout(1000) # Give agents time to move towards resources and potentially reproduce or die

        pop_after_settle = int(page.locator("#popDisplay").inner_text())
        assert pop_after_settle > 0, "Population should not immediately die off in normal conditions"

        # 4. Trigger Hazard (Sea Level Rise)
        print("Triggering Sea Level Rise...")
        page.evaluate("triggerHazard('sealevel')")

        # Verify alert
        assert page.locator("#alertOverlay").is_visible(), "Alert overlay should appear on hazard trigger"

        # Allow time for agents to drown or migrate inland
        page.wait_for_timeout(1500)

        pop_after_hazard = int(page.locator("#popDisplay").inner_text())
        print(f"Population after hazard: {pop_after_hazard}")

        # 5. Test Reset
        page.locator("#resetBtn").click()
        reset_pop = page.locator("#popDisplay").inner_text()
        assert int(reset_pop) == 50, "Population should reset to 50"

        print("All Human Settlement tests passed!")
        browser.close()

if __name__ == "__main__":
    test_human_settlement()