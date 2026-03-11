import os
from playwright.sync_api import sync_playwright

def test_stellar_phenomena():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        base_dir = "/app"
        file_path = f"file://{os.path.join(base_dir, 'Simulations/EarthSpaceSciences/StellarPhenomenaSimulator.html')}"

        print(f"Navigating to {file_path}")
        page.goto(file_path, wait_until="networkidle")

        # Set document to visible to ensure requestAnimationFrame fires
        page.evaluate("document.hidden = false;")

        # 1. Verify Tab 1 Elements
        print("Verifying Tab 1 elements...")
        assert page.locator("#mass-display").is_visible()
        initial_mass = page.locator("#mass-display").inner_text()
        assert "1.0 M" in initial_mass

        # Move slider
        page.evaluate("document.getElementById('mass-slider').value = '15.0'")
        page.evaluate("document.getElementById('mass-slider').dispatchEvent(new Event('input'))")
        mass_text = page.locator("#mass-display").inner_text()
        assert "15.0 M" in mass_text
        color_text = page.locator("#star-color-text").inner_text()
        assert "Blue-White" in color_text

        # 2. Verify Tab 2 (Fusion)
        print("Verifying Tab 2 elements...")
        page.locator("#tab-sim2").click()
        assert page.locator("#fusion-btn").is_visible()
        page.locator("#fusion-btn").click()
        page.wait_for_timeout(2000) # Wait for animation
        mass_status = page.locator("#mass-status").inner_text()
        assert "lost" in mass_status

        # 3. Verify Tab 3 (Fate)
        print("Verifying Tab 3 elements...")
        page.locator("#tab-sim3").click()
        assert page.locator("#fate-btn").is_visible()
        page.locator("#fate-btn").click()
        page.wait_for_timeout(3000) # Wait for animation
        assert page.locator("#fate-readout").is_visible()

        print("All Stellar Phenomena tests passed!")
        browser.close()

if __name__ == "__main__":
    test_stellar_phenomena()
