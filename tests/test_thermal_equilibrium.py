import os
import sys
import time
from playwright.sync_api import sync_playwright

def get_file_url():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Simulations", "PhysicalSciences", "ThermalEquilibriumSandbox.html"))
    if not os.path.exists(base_path):
        # Fallback for local vs container structure
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Simulations", "PhysicalScience", "ThermalEquilibriumSandbox.html"))
    return f"file://{base_path}"

def test_thermal_equilibrium():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_url = get_file_url()
        print(f"Loading {file_url}")
        page.goto(file_url, wait_until="networkidle")

        # Basic page checks
        assert "Thermal Equilibrium Sandbox" in page.title(), "Title mismatch"

        # Verify initial state of UI elements
        assert page.locator("#startBtn").is_visible()
        assert page.locator("#resetBtn").is_visible()
        assert page.locator("#tempChart").is_visible()

        # Check initial temps
        initial_temp_a = page.evaluate("window.simulationState.currentTempA")
        initial_temp_b = page.evaluate("window.simulationState.currentTempB")
        print(f"Initial Temp A: {initial_temp_a}, Temp B: {initial_temp_b}")
        assert initial_temp_a == 90
        assert initial_temp_b == 20

        # Run simulation
        print("Starting simulation...")
        page.click("#startBtn")

        # Wait a bit for simulation to run and finish
        # Given the logic, delta T should approach < 0.05
        # The loop runs via requestAnimationFrame

        # In headless, rAF might not fire normally. We added the hidden=false trick in the JS,
        # but just in case, let's explicitly evaluate to step it if necessary.
        # However, the script is set to run via rAF. Wait up to 5 seconds.

        # In Playwright headless mode, rAF might still be throttled or stop completely if not visible
        # Let's ensure it stays active by interacting or forcing it to run
        page.evaluate("document.hidden = false;")

        max_waits = 100 # increase wait up to 10 seconds
        equilibrium_reached = False

        for i in range(max_waits):
            time.sleep(0.1)
            is_running = page.evaluate("window.simulationState.isRunning")
            if not is_running:
                equilibrium_reached = True
                break

            # Optionally step the simulation manually if rAF is stuck
            # page.evaluate("if (window.simulationState.isRunning) { simulationStep(); }")

        if not equilibrium_reached:
            print("Warning: Simulation didn't auto-stop within 10 seconds, it might be running slow or rAF is throttled. Forcing stop.")
            page.evaluate("stopSimulation();")

        # Check final temperatures. They should be equal (or very close)
        final_temp_a = page.evaluate("window.simulationState.currentTempA")
        final_temp_b = page.evaluate("window.simulationState.currentTempB")

        print(f"Final Temp A: {final_temp_a}, Temp B: {final_temp_b}")

        # They should be roughly equal (delta < 0.1)
        assert abs(final_temp_a - final_temp_b) < 0.1, f"Temps didn't reach equilibrium: {final_temp_a} vs {final_temp_b}"

        # Click Reset and verify
        page.click("#resetBtn")
        reset_temp_a = page.evaluate("window.simulationState.currentTempA")
        assert reset_temp_a == 90, f"Reset failed, Temp A is {reset_temp_a}"

        print("All tests passed successfully.")
        browser.close()

if __name__ == "__main__":
    test_thermal_equilibrium()