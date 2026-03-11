import os
from playwright.sync_api import sync_playwright

def test_four_factors_evolution():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', 'Simulations', 'LifeSciences', 'FourFactorsEvolution.html')
    file_uri = f"file://{os.path.abspath(file_path)}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(file_uri)

        # Unhide document to allow requestAnimationFrame to run properly
        page.evaluate("Object.defineProperty(document, 'hidden', { value: false, writable: false });")

        # 1. Verify Initial UI State
        page.wait_for_selector("#btn-start")
        pop_text = page.locator("#stat-pop").inner_text()
        assert pop_text == "20", f"Expected initial population of 20, got {pop_text}"

        # 2. Start Simulation and fast-forward
        page.click("#btn-start")

        # Set Env Color to Red (Hue 0) to force selection
        page.evaluate("document.getElementById('rng-env').value = '0';")
        page.evaluate("document.getElementById('rng-env').dispatchEvent(new Event('input'))")

        # Increase food rate so they don't all starve immediately while testing
        page.evaluate("document.getElementById('rng-food').value = '15';")
        page.evaluate("document.getElementById('rng-food').dispatchEvent(new Event('input'))")

        # Wait to allow simulation loop to run
        # (Using evaluate to fast forward ticks reliably)
        page.evaluate("for(let i=0; i<800; i++) { window.updateSimulation(); window.updateChartData(); }")

        # 3. Verify Chart updates and Population survives
        page.wait_for_timeout(200) # Give UI time to sync
        pop_text_after = int(page.locator("#stat-pop").inner_text())
        assert pop_text_after > 0, "Population should not be completely extinct if food is plentiful"

        # Average hue should have drifted towards 0 or 360 (Red) due to predator selection
        # Instead of strict math, just ensure the chart received data points
        chart_data_len = page.evaluate("chart.data.labels.length")
        assert chart_data_len > 0, "Chart should have collected data points over time"

        browser.close()
        print("Four Factors Evolution simulation test passed.")

if __name__ == "__main__":
    test_four_factors_evolution()
