import os
from playwright.sync_api import sync_playwright

def test_newts_and_snakes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_path = 'file://' + os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'LifeSciences', 'NewtsAndSnakes.html'))

        page.route('**/*', lambda route: route.continue_() if route.request.url.startswith('file://') else route.abort())
        page.goto(file_path)

        # Verify initial generation
        gen_counter = page.locator('#generationCounter').inner_text()
        assert gen_counter == '0'

        # Set High Mutation Rate
        page.evaluate("document.getElementById('mutationSlider').value = 10")
        page.evaluate("document.getElementById('mutationSlider').dispatchEvent(new Event('input'))")

        # Run 10 generations. Without animation we just manually increment generation
        # (Though snake meals are dependent on the animation loop's 'update' collision detection)
        # We can still call updateSimulationGeneration, which might result in snakes dying since they don't get meals,
        # but the generation counter should still work.
        for _ in range(10):
            page.evaluate("window.updateSimulationGeneration()")

        gen_counter = page.locator('#generationCounter').inner_text()
        assert gen_counter == '10'

        browser.close()
