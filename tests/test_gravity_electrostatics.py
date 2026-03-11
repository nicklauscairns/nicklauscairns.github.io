import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        filepath = os.path.abspath('Simulations/PhysicalSciences/GravityAndElectrostaticsSimulator.html')
        url = f"file://{filepath}"

        await page.goto(url)
        await page.wait_for_timeout(1000)

        # log data test
        await page.evaluate("document.getElementById('btn-record-data').click()")
        await page.wait_for_timeout(500)

        data_len = await page.evaluate("state.data.length")
        print(f"Data array length: {data_len}")
        assert data_len > 0

        print("Gravity and Electrostatics Simulator test PASSED.")
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
