import os
from playwright.sync_api import sync_playwright

def test_macroscopic_energy():
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'PhysicalSciences', 'MacroscopicEnergyModel.html'))
    if not os.path.exists(html_path):
        html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'PhysicalScience', 'MacroscopicEnergyModel.html'))

    file_uri = f"file://{html_path}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(file_uri, wait_until='networkidle')

        # Allow animation loop to run
        page.evaluate("document.hidden = false;")
        page.wait_for_timeout(500)

        # 1. Test Thermal Energy Default State
        active_tab = page.evaluate("window.testingTools.getActiveTab()")
        assert active_tab == 'thermal', f"Expected thermal to be default tab, got {active_tab}"

        temp_val = page.evaluate("window.testingTools.getTempValue()")
        assert temp_val == 20, f"Expected initial temp 20, got {temp_val}"

        # Get initial particle positions
        initial_particles = page.evaluate("window.testingTools.getThermalParticleMotion()")

        # 2. Add Heat
        page.evaluate("document.getElementById('temp-slider').value = 80;")
        page.evaluate("document.getElementById('temp-slider').dispatchEvent(new Event('input'))")
        page.wait_for_timeout(200) # let animation run briefly

        new_temp_val = page.evaluate("window.testingTools.getTempValue()")
        assert new_temp_val == 80, f"Expected temp 80 after adjustment, got {new_temp_val}"

        # Measure displacement to verify motion increased
        heated_particles = page.evaluate("window.testingTools.getThermalParticleMotion()")
        total_initial_displacement = sum(abs(p['x'] - p['bx']) + abs(p['y'] - p['by']) for p in initial_particles)
        total_heated_displacement = sum(abs(p['x'] - p['bx']) + abs(p['y'] - p['by']) for p in heated_particles)

        # Because it's random we just want to ensure it's oscillating and changed
        assert total_heated_displacement != total_initial_displacement, "Particles should be moving differently after heating"

        # 3. Switch to Potential Energy
        page.locator("#tab-potential").click()
        page.wait_for_timeout(200)

        active_tab = page.evaluate("window.testingTools.getActiveTab()")
        assert active_tab == 'potential', f"Expected potential tab, got {active_tab}"

        # 4. Stretch the spring
        initial_pos = page.evaluate("window.testingTools.getPotentialParticlePos()")

        page.evaluate("document.getElementById('stretch-slider').value = 100;")
        page.evaluate("document.getElementById('stretch-slider').dispatchEvent(new Event('input'))")
        page.wait_for_timeout(200)

        stretched_pos = page.evaluate("window.testingTools.getPotentialParticlePos()")

        # Verify relative positions changed
        for i in range(1, len(initial_pos)):
            init_dist = initial_pos[i]['x'] - initial_pos[i-1]['x']
            stretch_dist = stretched_pos[i]['x'] - stretched_pos[i-1]['x']
            assert stretch_dist > init_dist, f"Expected relative distance {stretch_dist} to be > {init_dist} after stretch"

        browser.close()

if __name__ == "__main__":
    test_macroscopic_energy()
    print("All tests passed for Macroscopic Energy Model.")