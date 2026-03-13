from playwright.sync_api import sync_playwright
import os
import time

def test_imf():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        file_path = f"file://{os.path.abspath('Simulations/PhysicalSciences/IntermolecularForces.html')}"
        page.goto(file_path, wait_until="networkidle")

        # Bypass overlay
        page.evaluate("document.getElementById('planningOverlay').style.display = 'none';")
        time.sleep(0.5)
        # Verify initial state
        assert "Intermolecular Forces Investigation" in page.title()

        # Default is nonpolar


        # Test temperature slider causing boiling
        page.evaluate("document.getElementById('tempSlider').value = 90")
        page.locator("#tempSlider").dispatch_event("input")

        # Wait a tick for UI to update
        time.sleep(0.5)

        # Verify boiling overlay is shown
        assert "hidden" not in page.locator("#boilingOverlay").get_attribute("class")

        # Switch to Hydrogen Bonding
        page.locator("input[value='hbond']").click()
        time.sleep(0.5)

        assert page.locator("#imfType").inner_text() == "Hydrogen Bonding"
        page.locator("#recordDataBtn").click()
        time.sleep(0.1)
        assert page.locator("#bpValue").inner_text() == "100°C"

        print("Playwright test passed: IntermolecularForces logic functions correctly.")

        browser.close()

if __name__ == "__main__":
    test_imf()