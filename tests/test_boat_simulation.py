import asyncio
import os
import math
from playwright.async_api import async_playwright
from test_utils import setup_page

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        page = await setup_page(browser, 'PhysicalSciences/InteractiveBoatRiverCrossingSimulation.html')

        print("Testing pure `calculatePhysics` function...")

        # Setup standard input
        # dt, v_boat, v_river, theta_deg, boatPos, riverObserverPos, totalDistance_m, time, canvasWidth, scale

        # Test Case 1: dt capping
        # Passing dt=0.5 should get capped to 0.1
        dt_cap_res = await page.evaluate('''() => {
            return window.calculatePhysics(
                0.5, 2.0, 1.0, 0,
                {x: 400, y: 450}, {x: 0, y: 100},
                0, 0,
                800, 4.0
            );
        }''')
        assert dt_cap_res['dt'] == 0.1, f"Expected dt to be capped at 0.1, got {dt_cap_res['dt']}"
        print("Test Case 1 (dt capping) PASSED")

        # Test Case 2: Boat going straight up (0 degrees)
        # v_bw_x = 2.0 * sin(0) = 0
        # v_bw_y = -2.0 * cos(0) = -2.0
        # v_ws_x = 1.0, v_ws_y = 0
        # v_bs_x = 0 + 1.0 = 1.0
        # v_bs_y = -2.0 + 0 = -2.0
        # dt = 0.1
        # dist_m = sqrt(1^2 + (-2)^2) * 0.1 = sqrt(5) * 0.1 ~= 0.2236
        # scale = 4.0
        # newBoatPos_x = 400 + (1.0 * 4.0) * 0.1 = 400 + 0.4 = 400.4
        # newBoatPos_y = 450 + (-2.0 * 4.0) * 0.1 = 450 - 0.8 = 449.2
        straight_up_res = await page.evaluate('''() => {
            return window.calculatePhysics(
                0.1, 2.0, 1.0, 0,
                {x: 400, y: 450}, {x: 0, y: 100},
                0, 0,
                800, 4.0
            );
        }''')
        assert abs(straight_up_res['v_bs_x'] - 1.0) < 1e-5
        assert abs(straight_up_res['v_bs_y'] - (-2.0)) < 1e-5
        assert abs(straight_up_res['newBoatPos']['x'] - 400.4) < 1e-5
        assert abs(straight_up_res['newBoatPos']['y'] - 449.2) < 1e-5
        print("Test Case 2 (Straight up / 0 degrees) PASSED")

        # Test Case 3: Boat going right (90 degrees)
        # v_bw_x = 2.0 * sin(90) = 2.0
        # v_bw_y = -2.0 * cos(90) = 0
        # v_ws_x = 1.0, v_ws_y = 0
        # v_bs_x = 2.0 + 1.0 = 3.0
        # v_bs_y = 0 + 0 = 0
        # dt = 0.1
        # newBoatPos_x = 400 + (3.0 * 4.0) * 0.1 = 400 + 1.2 = 401.2
        # newBoatPos_y = 450 + (0 * 4.0) * 0.1 = 450
        right_res = await page.evaluate('''() => {
            return window.calculatePhysics(
                0.1, 2.0, 1.0, 90,
                {x: 400, y: 450}, {x: 0, y: 100},
                0, 0,
                800, 4.0
            );
        }''')
        assert abs(right_res['v_bs_x'] - 3.0) < 1e-5
        assert abs(right_res['v_bs_y'] - 0.0) < 1e-5
        assert abs(right_res['newBoatPos']['x'] - 401.2) < 1e-5
        assert abs(right_res['newBoatPos']['y'] - 450) < 1e-5
        print("Test Case 3 (Right / 90 degrees) PASSED")

        # Test Case 4: River observer wrap around
        # observer pos = 800, v_river = 1.0, canvas_width = 800
        # new pos = 800 + (1.0 * 4.0) * 0.1 = 800.4
        # Wait, canvas.width + 40 = 840, so it shouldn't wrap yet
        no_wrap_res = await page.evaluate('''() => {
            return window.calculatePhysics(
                0.1, 2.0, 1.0, 0,
                {x: 400, y: 450}, {x: 800, y: 100},
                0, 0,
                800, 4.0
            );
        }''')
        assert abs(no_wrap_res['newRiverObserverPos']['x'] - 800.4) < 1e-5

        # observer pos = 840, v_river = 1.0, canvas_width = 800
        # new pos = 840 + 0.4 = 840.4
        # Should wrap to -40
        wrap_res = await page.evaluate('''() => {
            return window.calculatePhysics(
                0.1, 2.0, 1.0, 0,
                {x: 400, y: 450}, {x: 840, y: 100},
                0, 0,
                800, 4.0
            );
        }''')
        assert abs(wrap_res['newRiverObserverPos']['x'] - (-40.0)) < 1e-5
        print("Test Case 4 (River Observer wrap around) PASSED")

        print("All Physics Logic Unit Tests PASSED!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
