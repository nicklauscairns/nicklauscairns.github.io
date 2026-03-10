import os
import time
from playwright.sync_api import sync_playwright

def get_file_url():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Simulations", "PhysicalSciences", "ElectromagnetismInduction.html"))
    if not os.path.exists(base_path):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Simulations", "PhysicalScience", "ElectromagnetismInduction.html"))
    return f"file://{base_path}"

def test_electromagnetism():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_url = get_file_url()
        print(f"Loading {file_url}")
        page.goto(file_url, wait_until="networkidle")

        # Tab 1: Electromagnet
        # Default: 0V, so B-field should be just background (~0.5)
        b_field_text = page.inner_text("#bFieldVal")
        assert "0.50" == b_field_text, f"Expected 0.50 background field, got {b_field_text}"

        # Increase voltage
        page.evaluate("document.getElementById('voltageSlider').value = '10';")
        page.evaluate("document.getElementById('voltageSlider').dispatchEvent(new Event('input'));")

        b_field_text_high = float(page.inner_text("#bFieldVal"))
        assert b_field_text_high > 0.5, f"Field didn't increase from baseline 0.5, got {b_field_text_high}"
        print(f"B-field correctly increased to {b_field_text_high} mT at 10V")

        # Tab 2: Induction
        page.click("#tab2-btn")

        # Ensure rAF fires
        page.evaluate("document.hidden = false;")

        # Current should be ~0 initially
        current_text = float(page.inner_text("#currentVal"))
        assert abs(current_text) < 0.1, f"Expected 0 initial current, got {current_text}"

        # Manually move magnet quickly using JS coordinates and Mouse Events
        # Magnet is #dragMagnet. We'll simulate a fast drag across the coil.

        box = page.locator("#dragMagnet").bounding_box()
        page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
        page.mouse.down()
        page.mouse.move(box["x"] + 200, box["y"] + box["height"] / 2, steps=10) # Fast move right
        page.mouse.up()

        # Wait a tick for physics loop
        time.sleep(0.1)

        current_spike = float(page.inner_text("#currentVal"))
        print(f"Induced current spike: {current_spike} A")
        assert abs(current_spike) > 0.0, f"Expected current spike, got {current_spike}"

        print("All tests passed successfully.")
        browser.close()

if __name__ == "__main__":
    test_electromagnetism()