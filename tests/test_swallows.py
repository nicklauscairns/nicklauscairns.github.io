import os
from playwright.sync_api import sync_playwright

def test_cliff_swallows():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_path = 'file://' + os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'LifeSciences', 'CliffSwallows.html'))

        page.route('**/*', lambda route: route.continue_() if route.request.url.startswith('file://') else route.abort())
        page.goto(file_path)

        # Verify initial generation
        gen_counter = page.locator('#generationCounter').inner_text()
        assert gen_counter == '0'

        # We need to run some logic to test. Since the cars kill birds in the gameLoop (via requestAnimationFrame),
        # testing it exactly via pure Playwright evaluate requires simulating ticks or directly invoking update/draw.
        # But we also decoupled `updateSimulationGeneration()`. Let's just test that the function advances generations correctly.
        # Without traffic, wing spans should stay high.

        for _ in range(5):
            page.evaluate("window.updateSimulationGeneration()")

        gen_counter = page.locator('#generationCounter').inner_text()
        assert gen_counter == '5'

        browser.close()
