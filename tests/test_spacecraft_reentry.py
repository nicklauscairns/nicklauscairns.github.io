from playwright.sync_api import sync_playwright
import os

def test_spacecraft_reentry():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Construct dynamic absolute path
        file_path = "file://" + os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'EngineeringTechnologyScience', 'SpacecraftReentrySimulation.html'))
        page.goto(file_path)
        page.wait_for_timeout(1000)

        # 1. Update inputs
        page.evaluate("document.getElementById('mass').value = '4000'; document.getElementById('mass').dispatchEvent(new Event('input'))")
        page.evaluate("document.getElementById('angle').value = '10'; document.getElementById('angle').dispatchEvent(new Event('input'))")
        page.wait_for_timeout(500)

        # 2. Acknowledge limitations modal before running
        page.evaluate("document.getElementById('open-modal-btn').click()")
        page.wait_for_timeout(500)
        page.evaluate("document.getElementById('close-modal-btn').click()")
        page.wait_for_timeout(500)

        # 3. Run sim
        page.evaluate("document.getElementById('run-simulation').click()")
        page.wait_for_timeout(2000) # Wait for simulation to finish

        # Verify
        status = page.locator('#mission-status').inner_text()
        print(f"Mission Status: {status}")
        assert status is not None and len(status) > 0, "Mission status text should be present."

        gforce = page.locator('#gforce-output').inner_text()
        print(f"G-Force: {gforce}")
        assert gforce is not None and gforce != "---", "G-Force should be calculated and present."

        print(f"Test complete.")
        browser.close()

if __name__ == "__main__":
    test_spacecraft_reentry()
