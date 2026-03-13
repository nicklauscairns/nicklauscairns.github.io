import os
from playwright.sync_api import sync_playwright

def test_gorongosa_elephants():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_path = 'file://' + os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'LifeSciences', 'GorongosaElephants.html'))

        # Block external requests to avoid timeouts
        page.route('**/*', lambda route: route.continue_() if route.request.url.startswith('file://') else route.abort())

        page.goto(file_path)

        # Override visibility for animations just in case
        page.evaluate("Object.defineProperty(document, 'hidden', { value: false, writable: false });")

        # Verify initial state
        gen_counter = page.locator('#generationCounter').inner_text()
        assert gen_counter == '0'

        # Set extreme poaching
        page.evaluate("document.getElementById('poachingSlider').value = 80")
        page.evaluate("document.getElementById('poachingSlider').dispatchEvent(new Event('input'))")

        # The logic is decoupled, so we can just call updateSimulationGeneration multiple times
        # Run 50 generations
        for _ in range(50):
            page.evaluate("window.updateSimulationGeneration()")

        gen_counter = page.locator('#generationCounter').inner_text()
        assert gen_counter == '50'

        # With extreme poaching, the tuskless population should increase significantly
        tuskless_count = int(page.locator('#tusklessCount').inner_text())
        tusked_count = int(page.locator('#tuskedCount').inner_text())

        # Tuskless should dominate after 50 generations of extreme poaching
        assert tuskless_count > tusked_count

        browser.close()
