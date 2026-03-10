import os
import sys
import time
from playwright.sync_api import sync_playwright

def get_file_url():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Simulations", "PhysicalSciences", "EggDropCrashCushion.html"))
    if not os.path.exists(base_path):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Simulations", "PhysicalScience", "EggDropCrashCushion.html"))
    return f"file://{base_path}"

def run_simulation_and_wait(page):
    page.click("#dropBtn")

    # Force document visible so rAF fires
    page.evaluate("document.hidden = false;")

    max_waits = 100
    finished = False

    for _ in range(max_waits):
        time.sleep(0.1)
        is_running = page.evaluate("window.simulationState.isRunning")
        if not is_running:
            finished = True
            break

    if not finished:
        print("Warning: Simulation didn't finish in time, forcing stop.")
        page.evaluate("finishSimulation();")

def test_egg_drop():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_url = get_file_url()
        print(f"Loading {file_url}")
        page.goto(file_url, wait_until="networkidle")

        assert "Collision Force Minimizer" in page.title()

        # Test Default Setting (Foam, 5m drop, 0.1kg). This should break (force > 50N).
        # Actually let's just run it and see.
        print("Running default simulation...")
        run_simulation_and_wait(page)

        is_broken = page.evaluate("window.simulationState.isBroken")
        max_force = page.evaluate("window.simulationState.maxForce")
        print(f"Default Drop: Max Force = {max_force:.1f} N. Broken = {is_broken}")

        # Reset
        page.click("#resetBtn")

        # Test a very soft, thick setting (Airbag, 1m drop, 0.05kg). Should survive.
        print("Setting up soft drop...")
        page.evaluate("document.getElementById('dropHeight').value = '1.0';")
        page.evaluate("document.getElementById('dropHeight').dispatchEvent(new Event('input'));")

        page.evaluate("document.getElementById('payloadMass').value = '0.05';")
        page.evaluate("document.getElementById('payloadMass').dispatchEvent(new Event('input'));")

        page.select_option("#materialType", "airbag")

        page.evaluate("document.getElementById('cushionThickness').value = '0.5';")
        page.evaluate("document.getElementById('cushionThickness').dispatchEvent(new Event('input'));")

        run_simulation_and_wait(page)

        is_broken = page.evaluate("window.simulationState.isBroken")
        max_force = page.evaluate("window.simulationState.maxForce")
        print(f"Soft Drop: Max Force = {max_force:.1f} N. Broken = {is_broken}")

        assert not is_broken, "Payload broke when it should have survived."
        assert max_force < 50, f"Force {max_force} was higher than 50N breaking point."

        # Test a hard, high drop (Concrete, 10m drop, 1kg). Should absolutely destroy it.
        page.click("#resetBtn")
        print("Setting up hard drop...")
        page.evaluate("document.getElementById('dropHeight').value = '10.0';")
        page.evaluate("document.getElementById('dropHeight').dispatchEvent(new Event('input'));")

        page.evaluate("document.getElementById('payloadMass').value = '1.0';")
        page.evaluate("document.getElementById('payloadMass').dispatchEvent(new Event('input'));")

        page.select_option("#materialType", "concrete")

        run_simulation_and_wait(page)

        is_broken_hard = page.evaluate("window.simulationState.isBroken")
        max_force_hard = page.evaluate("window.simulationState.maxForce")
        print(f"Hard Drop: Max Force = {max_force_hard:.1f} N. Broken = {is_broken_hard}")

        assert is_broken_hard, "Payload survived when it should have broken."
        assert max_force_hard > 50, f"Force {max_force_hard} was lower than 50N breaking point."

        print("All tests passed successfully.")
        browser.close()

if __name__ == "__main__":
    test_egg_drop()