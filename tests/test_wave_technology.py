import os
from playwright.sync_api import sync_playwright

def test_wave_technology():
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'PhysicalSciences', 'WaveInformationTechnology.html'))
    if not os.path.exists(html_path):
        html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'PhysicalScience', 'WaveInformationTechnology.html'))

    file_uri = f"file://{html_path}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(file_uri, wait_until='networkidle')

        page.evaluate("document.hidden = false;")
        page.wait_for_timeout(500)

        # 1. Test Solar Tab (Default)
        active_tab = page.evaluate("window.testingTools.getActiveTab()")
        assert active_tab == 'solar', f"Expected solar tab, got {active_tab}"

        intensity = page.evaluate("window.testingTools.getLightIntensity()")
        assert intensity == 50, f"Expected intensity 50, got {intensity}"

        # Turn off light
        page.evaluate("document.getElementById('intensity-slider').value = 0;")
        page.evaluate("document.getElementById('intensity-slider').dispatchEvent(new Event('input'))")
        page.wait_for_timeout(500) # Wait for photons to finish hitting
        page.evaluate("window.testingTools.clearElectrons();")
        page.wait_for_timeout(500) # Wait a bit to ensure absolutely no new ones spawn

        electrons = page.evaluate("window.testingTools.getElectrons()")
        assert len(electrons) == 0, f"Expected 0 electrons flowing when intensity is 0, got {len(electrons)}"

        # Turn light to max
        page.evaluate("document.getElementById('intensity-slider').value = 100;")
        page.evaluate("document.getElementById('intensity-slider').dispatchEvent(new Event('input'))")
        page.wait_for_timeout(1000) # let photons hit PN junction

        electrons_max = page.evaluate("window.testingTools.getElectrons()")
        assert len(electrons_max) > 0, f"Expected electrons flowing at 100 intensity, got {len(electrons_max)}"

        # 2. Test Fiber Optics Tab
        page.locator("#tab-fiber").click()
        page.wait_for_timeout(500)

        active_tab = page.evaluate("window.testingTools.getActiveTab()")
        assert active_tab == 'fiber', f"Expected fiber tab, got {active_tab}"

        fiber_success = page.evaluate("window.testingTools.getFiberStatus()")
        assert fiber_success is True, f"Expected fiber success at default 15 deg angle, got {fiber_success}"

        # Adjust angle to exceed critical angle (Total Internal Reflection fails)
        page.evaluate("document.getElementById('angle-slider').value = 40;")
        page.evaluate("document.getElementById('angle-slider').dispatchEvent(new Event('input'))")

        fiber_fail = page.evaluate("window.testingTools.getFiberStatus()")
        assert fiber_fail is False, f"Expected fiber to fail at 40 deg angle, got {fiber_fail}"

        browser.close()

if __name__ == "__main__":
    test_wave_technology()
    print("All tests passed for Wave Information Technology Model.")