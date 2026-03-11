import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        filepath = os.path.abspath('Simulations/PhysicalSciences/AlkaliMetalsPhenomenon.html')
        url = f"file://{filepath}"

        await page.goto(url)
        await page.wait_for_timeout(1000)

        # Check initial state
        selected_element = await page.evaluate("document.getElementById('elementName').textContent")
        print(f"Initial selected element text: {selected_element}")
        assert selected_element == 'Select a Metal'

        # Switch to Sodium
        await page.evaluate("dropMetal('Na')")
        await page.wait_for_timeout(500)
        selected_element = await page.evaluate("document.getElementById('elementName').textContent")
        print(f"Selected element after click: {selected_element}")
        assert selected_element == 'Sodium (Na)'

        # Verify animation state
        active_metal = await page.evaluate("activeMetal !== null")
        print(f"Is animating (activeMetal !== null): {active_metal}")
        assert active_metal == True

        # Wait a bit longer to make sure reaction resolves
        await page.wait_for_timeout(4000)

        print("Alkali Metals Phenomenon test PASSED.")
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
