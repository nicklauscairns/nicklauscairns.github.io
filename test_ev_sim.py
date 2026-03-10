import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        file_path = os.path.abspath('Simulations/EngineeringTechnologyScience/ElectricVehicleSimulation.html')

        # Read the HTML content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Strip out CDNs (Tailwind and Chart.js) to avoid timeout in sandbox
        content = content.replace('<script src="https://cdn.tailwindcss.com"></script>', '')
        content = content.replace('<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>', '')

        # Replace chart.js usage to not throw error since script is removed
        content = content.replace("const powerChart = new Chart", "const powerChart = { data: { datasets: [{ data: [] }] }, update: function() {} }; // new Chart")

        # We need to completely stub Chart since it's referenced directly
        content = content.replace("const ctx = document.getElementById('powerChart').getContext('2d');", "const ctx = {}; window.Chart = function() { return powerChart; };")

        # Load content into page
        await page.set_content(content, wait_until='load')

        # Verify initial state
        range_val = await page.locator('#out-range').text_content()
        print(f"Initial Range: {range_val} km")

        # Record a trial
        await page.locator('#btn-record').click()

        # Change slider
        await page.evaluate("const el = document.getElementById('battery-capacity'); el.value = 100; el.dispatchEvent(new Event('input', {bubbles: true}));")

        range_val_new = await page.locator('#out-range').text_content()
        print(f"New Range with 100kWh: {range_val_new} km")

        # Record another trial
        await page.locator('#btn-record').click()

        # Wait a moment
        await page.wait_for_timeout(1000)

        # Take screenshot
        screenshot_path = 'ev_sim_screenshot.png'
        await page.screenshot(path=screenshot_path, full_page=True)
        print(f"Saved screenshot to {screenshot_path}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())