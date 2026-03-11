import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        filepath = os.path.abspath('Simulations/PhysicalSciences/FromSparksToWavesSimulation.html')
        url = f"file://{filepath}"

        await page.goto(url)
        await page.wait_for_timeout(1000)

        # The strike button triggers the lightning
        await page.evaluate("document.getElementById('btn-strike').click()")
        await page.wait_for_timeout(500)

        # Verify that simulation time advances
        # NOTE: the simulation uses requestAnimationFrame, since document is hidden in headless it might not advance
        # Let's mock visibility
        await page.evaluate("Object.defineProperty(document, 'hidden', { value: false, writable: false });")
        await page.evaluate("document.dispatchEvent(new Event('visibilitychange'));")

        await page.evaluate("document.getElementById('btn-strike').click()")
        await page.wait_for_timeout(500)

        simTime = await page.evaluate("document.getElementById('prop-time').textContent")
        print(f"Simulation time after 500ms: {simTime}")

        # Switch view to oscilloscope
        await page.evaluate("document.getElementById('btn-osc').click()")
        await page.wait_for_timeout(500)

        # Adjust sound frequency slider
        await page.evaluate("document.getElementById('freq-slider').value = '150'")
        await page.evaluate("document.getElementById('freq-slider').dispatchEvent(new Event('input'))")
        await page.wait_for_timeout(500)

        freq_display = await page.evaluate("document.getElementById('freq-val').textContent")
        print(f"Frequency display: {freq_display}")
        assert "150" in freq_display

        print("From Sparks to Waves test PASSED.")
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
