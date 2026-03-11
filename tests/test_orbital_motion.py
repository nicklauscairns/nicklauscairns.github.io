import os
from playwright.sync_api import sync_playwright

def test_orbital_motion():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        base_dir = "/app"
        file_path = f"file://{os.path.join(base_dir, 'Simulations/EarthSpaceSciences/OrbitalMotion.html')}"

        print(f"Navigating to {file_path}")
        page.goto(file_path, wait_until="networkidle")

        # Set document to visible to ensure requestAnimationFrame fires
        page.evaluate("document.hidden = false;")

        # 1. Verify UI Elements
        print("Verifying UI elements...")
        assert page.locator("h1", has_text="Orbital Motion").is_visible()
        assert page.locator("#simCanvas").is_visible()
        assert page.locator("#dataChart").is_visible()

        # 2. Check initial readout
        initial_e = page.locator("#readoutE").inner_text()
        assert initial_e == "0.000", f"Initial e should be 0.000, got {initial_e}"

        # 3. Modify mass and check readout
        print("Changing star mass...")
        page.evaluate("document.getElementById('starMass').value = '2.0'")
        page.evaluate("document.getElementById('starMass').dispatchEvent(new Event('input'))")

        # Velocity multiplier is 1.0. Circular orbit velocity is sqrt(GM/r).
        # We start with v0 = vCirc * vMult = sqrt(G*1/1) * 1.0
        # If mass changes to 2.0 but v0 is recalculated to sqrt(G*2/1) * 1.0, e will still be 0.
        # Let's change velMultiplier to make it elliptical
        page.evaluate("document.getElementById('velMultiplier').value = '1.2'")
        page.evaluate("document.getElementById('velMultiplier').dispatchEvent(new Event('input'))")

        new_e = page.locator("#readoutE").inner_text()
        assert float(new_e) > 0.0, f"Eccentricity should increase, got {new_e}"

        # Check escape
        page.evaluate("document.getElementById('velMultiplier').value = '1.5'")
        page.evaluate("document.getElementById('velMultiplier').dispatchEvent(new Event('input'))")
        status = page.locator("#readoutStatus").inner_text()
        assert "Escape" in status

        print("All Orbital Motion tests passed!")
        browser.close()

if __name__ == "__main__":
    test_orbital_motion()
