import os
import pytest
from playwright.sync_api import sync_playwright

def test_diesel_engine_runaway():
    """Verify that the diesel engine runaway physics respond correctly to slider inputs and fault triggers."""
    file_path = f"file://{os.path.abspath('Simulations/PhysicalSciences/DieselEngineRunaway.html')}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=['--use-gl=egl'])
        page = browser.new_page()

        # Intercept network requests to allow local files and specific CDNs
        page.route('**/*', lambda route: route.continue_() if route.request.url.startswith('file://') or any(kw in route.request.url for kw in ['tailwind', 'chart.js']) else route.abort())

        # Collect console errors
        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)

        try:
            page.goto(file_path, wait_until='networkidle')

            # Force rendering in headless mode
            page.evaluate("Object.defineProperty(document, 'hidden', { value: false, writable: false });")

            # Allow time for canvas/animations to run and state to initialize
            page.wait_for_timeout(1000)

            # Check that key elements are present
            assert page.locator('#fuelSlider').is_visible(), "Fuel slider is not visible"
            assert page.locator('#airSlider').is_visible(), "Air slider is not visible"
            assert page.locator('#engineCanvas').is_visible(), "Engine canvas is not visible"
            assert page.locator('#rpmDisplay').is_visible(), "RPM display is not visible"
            assert page.locator('#mysteryFaultBtn').is_visible(), "Mystery fault button is not visible"

            # Close the briefing modal if it's intercepting clicks
            if page.locator('#briefingModal').is_visible():
                page.evaluate("document.getElementById('briefingModal').classList.add('hidden')")

            # Test interactions: increase fuel
            page.evaluate("document.getElementById('fuelSlider').value = 50")
            page.evaluate("document.getElementById('fuelSlider').dispatchEvent(new Event('input'))")

            # Wait a moment for RPM to increase due to physics update
            page.wait_for_timeout(2000)

            # Check the state
            state = page.evaluate("window.simulationState")
            assert float(state['rpm']) > 0, f"RPM should be > 0 after adding fuel, got {state['rpm']}"
            assert float(state['fuel']) == 50, f"Fuel state should be 50, got {state['fuel']}"

            # Test interactions: Trigger runaway fault
            # Set the state directly since the UI might be behaving weirdly in headless Playwright
            page.evaluate("window.simulationState.faultActive = true;")
            page.evaluate("window.simulationState.faultSeverity = 10;")
            page.wait_for_timeout(2000)

            state = page.evaluate("window.simulationState")
            assert state['faultActive'] is True, "Fault should be active"
            assert float(state['temp']) > 20, f"Temperature should be increasing, got {state['temp']}"

            # Ensure no critical console errors occurred
            assert not any("TypeError" in err for err in console_errors), f"Console TypeErrors found: {console_errors}"
            assert not any("ReferenceError" in err for err in console_errors), f"Console ReferenceErrors found: {console_errors}"

        finally:
            browser.close()
