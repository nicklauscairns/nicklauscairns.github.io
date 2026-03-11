from playwright.sync_api import sync_playwright
import os

def test_respiration():
    possible_paths = [
        "Simulations/LifeSciences/CellularRespiration.html",
        "../Simulations/LifeSciences/CellularRespiration.html",
        "/app/Simulations/LifeSciences/CellularRespiration.html"
    ]

    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = os.path.abspath(path)
            break

    if not file_path:
        raise FileNotFoundError("Could not find CellularRespiration.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{file_path}", wait_until="networkidle")

        # Need to explicitly tell playwright that document is visible so requestAnimationFrame runs
        page.evaluate("Object.defineProperty(document, 'hidden', {value: false, writable: false})")

        # 1. Verify Initial State
        assert page.locator("#energy-output").text_content() == "0 ATP"

        # Check inputs equation opacity (should be faded)
        input_classes = page.locator("#eq-inputs").get_attribute("class")
        assert "opacity-30" in input_classes

        # 2. Load Inputs
        page.locator("#btn-add-inputs").click()
        page.wait_for_timeout(100)

        # Verify inputs highlighted
        input_classes = page.locator("#eq-inputs").get_attribute("class")
        assert "opacity-100" in input_classes

        # React should now be enabled
        is_disabled = page.evaluate("document.getElementById('btn-react').disabled")
        assert is_disabled == False

        # 3. Run Reaction
        page.locator("#btn-react").click()

        # Wait for simulation to finish (set to 2.5s in JS)
        page.wait_for_timeout(3000)

        # Verify outputs highlighted
        output_classes = page.locator("#eq-outputs").get_attribute("class")
        assert "opacity-100" in output_classes

        # Verify Energy generated
        assert "~36 ATP" in page.locator("#energy-output").text_content()

        # Take screenshot for verification
        os.makedirs('/home/jules/verification', exist_ok=True)
        page.screenshot(path='/home/jules/verification/respiration_screenshot.png', full_page=True)

        browser.close()
        print("Cellular Respiration simulation test passed.")

if __name__ == "__main__":
    test_respiration()