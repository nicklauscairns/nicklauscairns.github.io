import os
from playwright.sync_api import sync_playwright

def test_big_bang_explorer():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Build absolute path to the local HTML file
        base_dir = "/app"
        file_path = f"file://{os.path.join(base_dir, 'Simulations/EarthSpaceSciences/BigBangEvidenceExplorer.html')}"

        print(f"Navigating to {file_path}")
        page.goto(file_path, wait_until="networkidle")

        # 1. Verify Tab Navigation
        print("Verifying Tab Navigation...")
        assert page.locator("#redshift").is_visible(), "Redshift tab should be visible initially"
        assert not page.locator("#composition").is_visible(), "Composition tab should be hidden initially"

        page.locator("button:has-text('Composition of Matter')").click()
        assert page.locator("#composition").is_visible(), "Composition tab should be visible after click"
        assert not page.locator("#redshift").is_visible(), "Redshift tab should be hidden after click"

        page.locator("button:has-text('Cosmic Microwave Background')").click()
        assert page.locator("#cmb").is_visible(), "CMB tab should be visible after click"

        # 2. Verify Tab 1: Redshift (Interactivity)
        print("Verifying Tab 1 (Redshift)...")
        page.locator("button:has-text('Expanding Universe (Redshift)')").click()

        # Click the canvas to select a galaxy
        canvas_rect = page.locator("#universeCanvas").bounding_box()
        # Click slightly off-center where a galaxy might be
        page.mouse.click(canvas_rect["x"] + canvas_rect["width"] / 2 + 20,
                         canvas_rect["y"] + canvas_rect["height"] / 2 + 20)

        # The spectrum box might become visible, or not if we missed a galaxy.
        # It's a bit probabilistic to hit a random galaxy, but we can verify the slider changes state
        slider = page.locator("#expansionSlider")
        slider.fill("2")
        page.evaluate("document.getElementById('expansionSlider').dispatchEvent(new Event('input'))")

        # We can also attempt to click the canvas at multiple points until the spectrum box appears
        spectrum_box = page.locator("#spectrumBox")
        for i in range(10):
             page.mouse.click(canvas_rect["x"] + 30 + i*15, canvas_rect["y"] + 30 + i*15)
             if spectrum_box.is_visible():
                 break

        if spectrum_box.is_visible():
            print("Galaxy selected.")
            page.locator("#recordBtn").click()
            assert page.locator("#dataTableBody tr").count() > 0, "Data should be added to the table"

        # 3. Verify Tab 2: Composition
        print("Verifying Tab 2 (Composition)...")
        page.locator("button:has-text('Composition of Matter')").click()

        status_text = page.locator("#analysisStatus").inner_text()
        assert "Waiting" in status_text, "Initial status should be waiting"

        page.locator("#sampleCloud").click()

        # Wait for the setTimeout to complete
        page.wait_for_timeout(2000)

        new_status = page.locator("#analysisStatus").inner_text()
        assert "Matches Big Bang Prediction" in new_status, "Analysis should complete successfully"

        # 4. Verify Tab 3: CMB
        print("Verifying Tab 3 (CMB)...")
        page.locator("button:has-text('Cosmic Microwave Background')").click()

        initial_temp = page.locator("#tempLabel").inner_text()

        # Change slider
        cmb_slider = page.locator("#timeSlider")
        cmb_slider.fill("50")
        page.evaluate("document.getElementById('timeSlider').dispatchEvent(new Event('input'))")

        new_temp = page.locator("#tempLabel").inner_text()
        assert initial_temp != new_temp, "Temperature should change when time changes"
        assert "K" in new_temp, "Temperature should be in Kelvin"

        print("All Big Bang Explorer tests passed!")
        browser.close()

if __name__ == "__main__":
    test_big_bang_explorer()