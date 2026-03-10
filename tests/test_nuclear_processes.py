from playwright.sync_api import sync_playwright
import os
import time

def test_nuclear_processes():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        file_path = f"file://{os.path.abspath('Simulations/PhysicalSciences/NuclearProcesses.html')}"
        page.goto(file_path, wait_until="networkidle")

        # Verify initial state (Alpha)
        assert "Nuclear Processes" in page.title()
        assert "Alpha" in page.locator("#processTitle").inner_text()

        # Test Alpha Reaction
        page.click("#triggerBtn")
        time.sleep(2) # wait for animation

        # Equation should be fully populated
        assert "Th" in page.locator("#equationDisplay").inner_text()
        assert page.is_visible("#resetBtn")

        # Test Fission
        page.click("input[value='fission']")
        time.sleep(0.5)
        assert "Fission" in page.locator("#processTitle").inner_text()

        page.click("#triggerBtn")
        time.sleep(2)
        assert "Ba" in page.locator("#equationDisplay").inner_text()

        # Test Fusion
        page.click("input[value='fusion']")
        time.sleep(0.5)
        assert "Fusion" in page.locator("#processTitle").inner_text()

        page.click("#triggerBtn")
        time.sleep(2)
        assert "He" in page.locator("#equationDisplay").inner_text()

        print("Playwright test passed: NuclearProcesses logic functions correctly.")

        browser.close()

if __name__ == "__main__":
    test_nuclear_processes()