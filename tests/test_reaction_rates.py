from playwright.sync_api import sync_playwright
import time
import os

def test_reaction_rates():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Build absolute file path to the local HTML file
        file_path = f"file://{os.path.abspath('Simulations/PhysicalSciences/ReactionRatesSimulation.html')}"
        page.goto(file_path, wait_until="networkidle")

        # Verify initial state
        assert "Reaction Rates Simulation" in page.title()
        assert page.locator("#startBtn").is_visible()
        assert page.locator("#temperatureSlider").is_visible()

        # Verify initial particles in state
        initial_counts = page.evaluate("window.simState.counts")
        assert initial_counts['A'] == 50
        assert initial_counts['B'] == 50
        assert initial_counts['AB'] == 0

        # Adjust settings to maximize reaction probability
        # High Temperature
        page.evaluate("document.getElementById('temperatureSlider').value = 600")
        page.locator("#temperatureSlider").dispatch_event("input")
        # Low Activation Energy
        page.evaluate("document.getElementById('activationEnergySlider').value = 10")
        page.locator("#activationEnergySlider").dispatch_event("input")
        # Max Concentration
        page.evaluate("document.getElementById('concentrationASlider').value = 100")
        page.locator("#concentrationASlider").dispatch_event("input")
        page.evaluate("document.getElementById('concentrationBSlider').value = 100")
        page.locator("#concentrationBSlider").dispatch_event("input")

        counts_before_start = page.evaluate("window.simState.counts")
        assert counts_before_start['A'] == 100
        assert counts_before_start['B'] == 100

        # Need to ensure window is visible for requestAnimationFrame to fire in headless chromium
        page.evaluate("document.hidden = false")

        # Start simulation
        page.click("#startBtn")

        # In some headless environments, requestAnimationFrame might be throttled or not run if the page is not visible.
        # We can manually pump the simulation loop to simulate 2 seconds passing.
        page.evaluate('''
            const step = 16.666;
            for(let i=0; i < 120; i++) {
                window.simState.lastFrameTime = performance.now() - step;
                window.simulationLoop(performance.now());
            }
        ''')

        # Pause simulation
        page.click("#pauseBtn")

        # Verify reactions occurred
        counts_after = page.evaluate("window.simState.counts")
        assert counts_after['A'] < 100
        assert counts_after['B'] < 100
        assert counts_after['AB'] > 0

        # Verify conservation of mass (atoms)
        assert counts_after['A'] + counts_after['AB'] == 100
        assert counts_after['B'] + counts_after['AB'] == 100

        # Verify data table logged rows
        row_count = page.locator("#dataTable tbody tr").count()
        assert row_count > 0

        print("Playwright test passed: ReactionRatesSimulation runs, particles react, and data is logged.")

        browser.close()

if __name__ == "__main__":
    test_reaction_rates()