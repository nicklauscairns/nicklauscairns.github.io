import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=['--use-gl=egl'])
        page = await browser.new_page()

        # Intercept network requests to allow local file access
        # Also need jsdelivr for OrbitControls.js
        await page.route("**/*", lambda route: route.continue_() if route.request.url.startswith("file://") or route.request.url.startswith("https://cdnjs.cloudflare.com/ajax/libs/three.js/") or route.request.url.startswith("https://cdn.tailwindcss.com") or route.request.url.startswith("https://cdn.jsdelivr.net") else route.abort())

        file_path = os.path.abspath("Simulations/PhysicalSciences/WaveSuperposition3D.html")
        print(f"Loading {file_path}...")

        page.on("console", lambda msg: print(f"Browser console: {msg.text}"))

        await page.goto(f"file://{file_path}", wait_until="networkidle")

        # Wait a bit to ensure Three.js initializes
        await page.wait_for_timeout(2000)

        await page.screenshot(path="screenshot_frontend_final2.png")
        print("Screenshot saved to screenshot_frontend_final2.png")

        await browser.close()

asyncio.run(main())
