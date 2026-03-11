import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        filepath = os.path.abspath('Simulations/PhysicalSciences/StageLightingSimulator.html')
        url = f"file://{filepath}"

        await page.goto(url)
        await page.wait_for_timeout(1000)

        # Check initial state
        countA = await page.evaluate("state.A")
        countB = await page.evaluate("state.B")
        print(f"Initial state A: {countA}, B: {countB}")
        assert countA == 1
        assert countB == 1

        # Add bulb to Track A (Series)
        await page.evaluate("updateBulbs('A', 1)")
        await page.wait_for_timeout(500)
        countA = await page.evaluate("state.A")
        print(f"State A after click: {countA}")
        assert countA == 2

        # Check current/power for Series (A)
        # V = 120, R_total = 2 * 24 = 48
        # I = 120 / 48 = 2.5 A
        # P = I^2 * R = 2.5^2 * 24 = 6.25 * 24 = 150 W
        currentA = await page.evaluate("document.getElementById('current-A').innerText")
        powerA = await page.evaluate("document.getElementById('power-A').innerText")
        print(f"Track A - Current: {currentA}, Power: {powerA}")
        assert "2.50 A" in currentA
        assert "150 W" in powerA

        # Add bulb to Track B (Parallel)
        await page.evaluate("updateBulbs('B', 1)")
        await page.wait_for_timeout(500)
        countB = await page.evaluate("state.B")
        print(f"State B after click: {countB}")
        assert countB == 2

        # Check current/power for Parallel (B)
        # V = 120 across each bulb
        # Total I = 2 * (120 / 24) = 2 * 5 = 10 A
        # P per bulb = V^2 / R = 120^2 / 24 = 14400 / 24 = 600 W
        currentB = await page.evaluate("document.getElementById('current-B').innerText")
        powerB = await page.evaluate("document.getElementById('power-B').innerText")
        print(f"Track B - Current: {currentB}, Power: {powerB}")
        assert "10.00 A" in currentB
        assert "600 W" in powerB

        print("Stage Lighting Simulator test PASSED.")
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
