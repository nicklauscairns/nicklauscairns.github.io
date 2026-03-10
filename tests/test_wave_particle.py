import os
from playwright.sync_api import sync_playwright

def test_wave_particle():
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'PhysicalSciences', 'WaveParticleDuality.html'))
    if not os.path.exists(html_path):
        html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'PhysicalScience', 'WaveParticleDuality.html'))

    file_uri = f"file://{html_path}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(file_uri, wait_until='networkidle')

        # Allow animation loop to run
        page.evaluate("document.hidden = false;")
        page.wait_for_timeout(500)

        # 1. Test Wave Model Tab (Default)
        active_tab = page.evaluate("window.testingTools.getActiveTab()")
        assert active_tab == 'wave', f"Expected wave tab by default, got {active_tab}"

        slit_spacing = page.evaluate("window.testingTools.getSlitSpacing()")
        assert slit_spacing == 40, f"Expected default slit spacing 40, got {slit_spacing}"

        # Adjust slits
        page.evaluate("document.getElementById('slit-slider').value = 80;")
        page.evaluate("document.getElementById('slit-slider').dispatchEvent(new Event('input'))")

        new_slit = page.evaluate("window.testingTools.getSlitSpacing()")
        assert new_slit == 80, f"Expected slit 80, got {new_slit}"

        # Verify text label changed
        slit_val_text = page.locator("#slit-val").inner_text()
        assert "Wide" in slit_val_text, f"Expected 'Wide' label for 80 spacing, got {slit_val_text}"

        # 2. Test Particle Model Tab
        page.locator("#tab-particle").click()
        page.wait_for_timeout(500)

        active_tab = page.evaluate("window.testingTools.getActiveTab()")
        assert active_tab == 'particle', f"Expected particle tab, got {active_tab}"

        freq = page.evaluate("window.testingTools.getFrequency()")
        assert freq == 700, f"Expected default freq 700 (Red), got {freq}"

        # Run red light for a bit (below threshold)
        page.wait_for_timeout(1000)
        electrons_ejected = page.evaluate("window.testingTools.getEjectedElectronsCount()")
        assert electrons_ejected == 0, f"Red light (700nm) should eject NO electrons, got {electrons_ejected}"

        # Adjust to Blue light (above threshold)
        page.evaluate("document.getElementById('freq-slider').value = 400;")
        page.evaluate("document.getElementById('freq-slider').dispatchEvent(new Event('input'))")

        new_freq = page.evaluate("window.testingTools.getFrequency()")
        assert new_freq == 400, f"Expected freq 400 (Blue), got {new_freq}"

        # Run blue light for a bit
        page.wait_for_timeout(2000)
        electrons_ejected_blue = page.evaluate("window.testingTools.getEjectedElectronsCount()")
        assert electrons_ejected_blue > 0, f"Blue light (400nm) should eject electrons, got {electrons_ejected_blue}"

        browser.close()

if __name__ == "__main__":
    test_wave_particle()
    print("All tests passed for Wave-Particle Duality Model.")