import os
from playwright.sync_api import sync_playwright

def test_orbital_motion2():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        base_dir = "/app"
        file_path = f"file://{os.path.join(base_dir, 'Simulations/EarthSpaceSciences/OrbitalMotion2.html')}"

        print(f"Navigating to {file_path}")
        page.goto(file_path, wait_until="networkidle")

        # Set document to visible to ensure requestAnimationFrame fires
        page.evaluate("document.hidden = false;")

        # 1. Verify UI Elements
        print("Verifying UI elements...")
        assert page.locator("h1", has_text="Orbital Motion & Kepler's Laws").is_visible()

        print("All Orbital Motion 2 tests passed!")
        browser.close()

if __name__ == "__main__":
    test_orbital_motion2()
