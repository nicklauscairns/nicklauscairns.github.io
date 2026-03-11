import os
from playwright.sync_api import sync_playwright

def test_ecosystem_resilience():
    # Construct the file path relative to the repo root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', 'Simulations', 'LifeSciences', 'EcosystemResilience.html')
    file_uri = f"file://{file_path}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the HTML file
        page.goto(file_uri)

        # Override hidden state to ensure requestAnimationFrame fires
        page.evaluate("Object.defineProperty(document, 'hidden', { value: false, writable: false });")

        # 1. Verify UI Elements load without JS errors
        page.wait_for_selector("#btn-start")
        page.wait_for_selector("#populationChart")
        page.wait_for_selector("#stat-plants")

        # Get initial stats
        initial_plants = int(page.locator("#stat-plants").inner_text().replace(',', ''))
        assert initial_plants == 1000, f"Expected initial plants 1000, got {initial_plants}"

        # 2. Test Modest Disturbance
        page.evaluate("window.simulationState.running = true")
        page.evaluate("window.applyDisturbance('modest')")

        # Wait a bit for the simulation to update (modest disturbance reduces K, populations should fall)
        page.wait_for_timeout(500)

        # Since requestAnimationFrame timing varies, we assert bounded states
        mid_plants = int(page.locator("#stat-plants").inner_text().replace(',', ''))
        assert mid_plants < initial_plants, "Modest disturbance should reduce plant population initially"

        # Modest disturbance timer is 200 frames. Fast forward time to see recovery
        page.evaluate("for(let i=0; i<300; i++) { window.updatePopulations(); }")

        # Wait a bit for DOM to update
        page.wait_for_timeout(200)

        recovered_plants = int(page.locator("#stat-plants").inner_text().replace(',', ''))
        assert recovered_plants > mid_plants, "Populations should begin recovering after modest disturbance (resilience)"

        # 3. Test Extreme Disturbance
        page.evaluate("window.applyDisturbance('extreme')")
        page.wait_for_timeout(200)

        extreme_plants = int(page.locator("#stat-plants").inner_text().replace(',', ''))
        # Extreme disturbance instantly chops population drastically (plants *= 0.1)
        assert extreme_plants < recovered_plants / 2, "Extreme disturbance should drastically slash populations"

        browser.close()
        print("Ecosystem Resilience simulation Playwright tests passed.")

if __name__ == "__main__":
    test_ecosystem_resilience()
