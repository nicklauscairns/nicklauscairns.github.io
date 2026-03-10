import asyncio
import os
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        filepath = os.path.abspath('Simulations/PhysicalSciences/ConservationOfMomentumSimulation.html')
        url = f"file://{filepath}"

        with open(filepath, 'r') as f:
            content = f.read()

        content = content.replace('<script src="https://cdn.tailwindcss.com"></script>', '')

        await page.set_content(content, wait_until="load")

        # Scenario 1: Elastic Collision (Default inputs)
        # m1=1.0, m2=1.5, v1=2.0, v2=-1.0, e=1.0
        # Expected final velocities:
        # m1 + m2 = 2.5
        # v1f = (1-1.5)*2/2.5 + 2*1.5*(-1)/2.5 = -0.5*2/2.5 - 3/2.5 = -1/2.5 - 3/2.5 = -4/2.5 = -1.6
        # v2f = (1.5-1)*(-1)/2.5 + 2*1*2/2.5 = 0.5*(-1)/2.5 + 4/2.5 = -0.5/2.5 + 4/2.5 = 3.5/2.5 = 1.4

        print("Testing Default Setup (Elastic Collision)")

        # Click start
        start_btn = await page.query_selector('#start-btn')
        await start_btn.click()

        # Wait until a collision happens (hasCollided becomes true)
        print("Waiting for collision...")
        while True:
            has_collided = await page.evaluate("state.hasCollided")
            if has_collided:
                break
            await page.wait_for_timeout(100)

        await page.wait_for_timeout(100) # Give UI time to update

        v1f_val = await page.evaluate("cart1.v")
        v2f_val = await page.evaluate("cart2.v")

        print(f"After Collision -> v1f: {v1f_val:.2f}, v2f: {v2f_val:.2f}")
        assert abs(v1f_val - (-1.6)) < 0.01, f"Expected v1f=-1.6, got {v1f_val}"
        assert abs(v2f_val - 1.4) < 0.01, f"Expected v2f=1.4, got {v2f_val}"
        print("Velocities match physics equations.")

        # Verify log table row is added
        row_count = await page.evaluate("document.getElementById('log-table-body').children.length")
        print(f"Rows in log table: {row_count}")
        assert row_count == 1, "Expected 1 row in the log table"

        # Check total momentum conservation
        # Initial: p1 = 1*2 = 2.0, p2 = 1.5*(-1) = -1.5 => Total Pi = 0.5
        # Final: pf1 = 1*(-1.6) = -1.6, pf2 = 1.5*1.4 = 2.1 => Total Pf = 0.5
        pi_ui = await page.evaluate("document.getElementById('metric-pi').textContent")
        pf_ui = await page.evaluate("document.getElementById('metric-pf').textContent")
        print(f"Momentum Initial: {pi_ui}, Momentum Final: {pf_ui}")
        assert pi_ui == pf_ui, "Momentum is not conserved in UI!"

        print("Physics test PASSED.")
        await browser.close()

asyncio.run(main())
