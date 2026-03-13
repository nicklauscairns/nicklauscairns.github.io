import asyncio
import os
from playwright.async_api import async_playwright
from test_utils import setup_page

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        page = await setup_page(browser, 'PhysicalSciences/ConservationOfMomentumSimulation.html')
        print("Loading Simulation")

        # Check if the canvas exists
        canvas = await page.query_selector('#sim-canvas')
        if canvas:
            print("Canvas element found.")
        else:
            print("Canvas element NOT found.")

        # Check start button
        start_btn = await page.query_selector('#start-btn')
        if start_btn:
            print("Start button found.")
        else:
            print("Start button NOT found.")

        # Let's run a short simulation check
        print("Clicking start...")
        await start_btn.click()
        await page.wait_for_timeout(1000) # wait 1 second

        # Check if pause is enabled now
        pause_disabled = await page.evaluate("document.getElementById('pause-btn').disabled")
        print(f"Pause button disabled: {pause_disabled}")

        await browser.close()

asyncio.run(main())
