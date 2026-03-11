import os
from playwright.sync_api import sync_playwright

def test_greenhouse_effect():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        base_dir = "/app"
        file_path = f"file://{os.path.join(base_dir, 'Simulations/EarthSpaceSciences/GreenhouseEffect.html')}"

        print(f"Navigating to {file_path}")
        page.goto(file_path, wait_until="networkidle")

        # Set document to visible to ensure requestAnimationFrame fires
        page.evaluate("document.hidden = false;")

        # 1. Verify UI Elements
        print("Verifying UI elements...")
        assert page.locator("h1", has_text="Earth's Energy Budget").is_visible()
        assert page.locator("#macroCanvas").is_visible()
        assert page.locator("#tempChart").is_visible()

        # 2. Check initial readouts
        initial_temp = page.locator("#globalTemp").inner_text()
        assert "15.0" in initial_temp

        # 3. Modify GHG concentration
        print("Changing GHG concentration...")
        page.evaluate("document.getElementById('ghgSlider').value = '1000'")
        page.evaluate("document.getElementById('ghgSlider').dispatchEvent(new Event('input'))")

        # Click play to let simulation run
        page.locator("#btn-play-pause").click()
        page.wait_for_timeout(2000)
        page.locator("#btn-play-pause").click()

        new_temp = page.locator("#globalTemp").inner_text()
        assert float(new_temp.split()[0]) > 15.0, f"Temperature should increase due to GHG, got {new_temp}"

        # 4. Decrease Solar intensity
        print("Changing Solar Intensity...")
        page.evaluate("document.getElementById('solarSlider').value = '80'")
        page.evaluate("document.getElementById('solarSlider').dispatchEvent(new Event('input'))")

        page.locator("#btn-play-pause").click()
        page.wait_for_timeout(2000)
        page.locator("#btn-play-pause").click()

        final_temp = page.locator("#globalTemp").inner_text()
        assert float(final_temp.split()[0]) < float(new_temp.split()[0]), f"Temperature should decrease due to low solar intensity, got {final_temp}"

        # 5. Check data logging
        page.locator("#btn-record").click()
        assert page.locator("#dataTableBody tr").count() == 1

        print("All Greenhouse Effect tests passed!")
        browser.close()

if __name__ == "__main__":
    test_greenhouse_effect()
