import os
from playwright.sync_api import sync_playwright

def test_water_properties():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        base_dir = "/app"
        file_path = f"file://{os.path.join(base_dir, 'Simulations/EarthSpaceSciences/WaterPropertiesEarthProcesses.html')}"

        print(f"Navigating to {file_path}")
        page.goto(file_path, wait_until="networkidle")

        # Set document to visible to ensure requestAnimationFrame fires
        page.evaluate("document.hidden = false;")

        # --- Test Lab 1: Frost Wedging ---
        print("Testing Frost Wedging...")
        assert page.locator("#tab-frost").is_visible()

        # Need high water volume to fracture
        page.evaluate("document.getElementById('waterSlider').value = '100'")
        page.evaluate("document.getElementById('waterSlider').dispatchEvent(new Event('input'))")

        # Lower temp to deep freezing to increase expansion rate
        page.evaluate("document.getElementById('tempSlider').value = '-20'")
        page.evaluate("document.getElementById('tempSlider').dispatchEvent(new Event('input'))")

        # Wait for strain to build up and fracture
        page.wait_for_timeout(4000) # give it time for ice expansion and strain exponential smoothing

        frost_state = page.evaluate("window.frostState")
        print(f"Frost state: {frost_state}")
        assert frost_state["strain"] > 0, "Rock strain should increase when freezing"
        assert frost_state["fractured"] == True, "Rock should fracture under prolonged freezing with high water volume"

        # --- Test Lab 2: Chemical Weathering ---
        print("Testing Chemical Weathering...")
        page.locator("button", has_text="Chemical Weathering").click()
        page.wait_for_timeout(500)
        assert page.locator("#tab-dissolve").is_visible()

        # Drop pH to highly acidic
        page.evaluate("document.getElementById('phSlider').value = '4.0'")
        page.evaluate("document.getElementById('phSlider').dispatchEvent(new Event('input'))")

        page.wait_for_timeout(1000)

        chem_state = page.evaluate("window.chemState")
        assert chem_state["mass"] < 100.0, f"Limestone mass should decrease in acidic water, current: {chem_state['mass']}"

        # --- Test Lab 3: Stream Transport ---
        print("Testing Stream Transport...")
        page.locator("button", has_text="Stream Transport").click()
        page.wait_for_timeout(500)
        assert page.locator("#tab-stream").is_visible()

        # Dump sediments
        page.locator("text=Dump Sediments").click()

        # Low velocity (should only move sand, maybe gravel, not cobbles)
        page.evaluate("document.getElementById('velSlider').value = '50'")
        page.evaluate("document.getElementById('velSlider').dispatchEvent(new Event('input'))")

        page.wait_for_timeout(500)
        stream_state_low = page.evaluate("window.streamState")

        # High velocity (should move everything)
        page.evaluate("document.getElementById('velSlider').value = '200'")
        page.evaluate("document.getElementById('velSlider').dispatchEvent(new Event('input'))")

        page.wait_for_timeout(500)
        stream_state_high = page.evaluate("window.streamState")

        print(f"Low vel moving: {stream_state_low}")
        print(f"High vel moving: {stream_state_high}")

        assert stream_state_high["particlesMoving"] > stream_state_low["particlesMoving"], "Higher velocity should move more particles"
        assert stream_state_high["cobbleMoving"] > stream_state_low["cobbleMoving"] or stream_state_high["cobbleMoving"] > 0, "High velocity should move heavy cobbles"

        print("All Water Properties tests passed!")
        browser.close()

if __name__ == "__main__":
    test_water_properties()