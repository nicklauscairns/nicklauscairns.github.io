import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Handle routing to avoid external CDN timeouts, allowing tailwind
        await page.route("**/*", lambda route: route.continue_() if route.request.url.startswith("file://") or "tailwind" in route.request.url else route.abort())

        filepath = os.path.abspath("Simulations/EarthSpaceSciences/ConnecticutRiverValleyRift.html")
        await page.goto(f"file://{filepath}")

        # Wait for canvas to load
        await page.wait_for_selector("#sim-canvas")

        # Check initial state
        state = await page.evaluate("window.simulationState")
        assert state['timeMa'] == 220, "Initial time should be 220"

        # Test slider update
        await page.evaluate("""
            const slider = document.getElementById('time-slider');
            slider.value = 195;
            slider.dispatchEvent(new Event('input'));
        """)

        state_after_input = await page.evaluate("window.simulationState")
        assert state_after_input['timeMa'] == 195, "Time should update after slider input"

        # Test if title updated
        title = await page.evaluate("document.getElementById('event-title').innerText")
        assert "Sedimentation" in title or "Pangea" in title or "Metacomet" in title, f"Title updated unexpectedly: {title}"

        # Test Play button
        await page.click("#btn-play")

        # Wait for a brief moment for animation to run
        await page.wait_for_timeout(100)

        state_after_play = await page.evaluate("window.simulationState")
        assert state_after_play['timeMa'] < 195, "Time should decrease after pressing play"

        # Capture a screenshot
        os.makedirs("/home/jules/verification", exist_ok=True)
        await page.screenshot(path="/home/jules/verification/connecticut_rift_sim.png")

        print("Frontend verification passed successfully.")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
