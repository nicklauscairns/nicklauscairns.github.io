import os
import math
from playwright.sync_api import sync_playwright

def test_calculate_kinematics():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Try PhysicalScience first (for reviewer environment), then fallback to PhysicalSciences (local)
        filepath = os.path.abspath('Simulations/PhysicalScience/ProjectileMotionSimulation.html')
        if not os.path.exists(filepath):
            filepath = os.path.abspath('Simulations/PhysicalSciences/ProjectileMotionSimulation.html')

        url = f"file://{filepath}"

        page.goto(url, wait_until="networkidle")

        def test_kinematics(t, params_str, expected, tol=0.01):
            page.evaluate(f"simState.params = {params_str}")
            state = page.evaluate(f"calculateKinematics({t})")

            for key in expected:
                assert abs(state[key] - expected[key]) < tol, f"Failed for {key} at t={t}: expected {expected[key]}, got {state[key]}"
            print(f"Pass: t={t}, params={params_str} -> {state}")

        # Test Case 1: Horizontal launch from a height
        params1 = "{ v0: 10, angle: 0, h0: 20, vc: 0, g: 10 }"
        t1 = 1.0
        expected1 = {"x": 10, "y": 15, "vx": 10, "vy": -10, "cart_x": 0}
        test_kinematics(t1, params1, expected1)

        # Test Case 2: Angled launch with a moving cart
        params2 = "{ v0: 20, angle: 30, h0: 0, vc: 5, g: 9.8 }"
        t2 = 2.0
        vx0_2 = 5 + 20 * math.cos(30 * math.pi / 180)
        vy0_2 = 20 * math.sin(30 * math.pi / 180)

        expected2 = {
            "x": vx0_2 * t2,
            "y": 10 * t2 - 0.5 * 9.8 * t2 * t2,
            "vx": vx0_2,
            "vy": 10 - 9.8 * t2,
            "cart_x": 10
        }
        test_kinematics(t2, params2, expected2)

        # Test Case 3: Vertical launch
        params3 = "{ v0: 15, angle: 90, h0: 0, vc: 0, g: 9.8 }"
        t3 = 1.5
        expected3 = {
            "x": 0,
            "y": 11.475,
            "vx": 0,
            "vy": 0.3,
            "cart_x": 0
        }
        test_kinematics(t3, params3, expected3)

        print("All kinematics tests PASSED.")

        browser.close()

if __name__ == "__main__":
    test_calculate_kinematics()
