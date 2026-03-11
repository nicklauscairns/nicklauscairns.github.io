from playwright.sync_api import sync_playwright
import os

def test_aerobic_anaerobic():
    possible_paths = [
        "Simulations/LifeSciences/AerobicAnaerobic.html",
        "../Simulations/LifeSciences/AerobicAnaerobic.html",
        "/app/Simulations/LifeSciences/AerobicAnaerobic.html"
    ]

    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = os.path.abspath(path)
            break

    if not file_path:
        raise FileNotFoundError("Could not find AerobicAnaerobic.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{file_path}", wait_until="networkidle")

        # 1. Verify Initial State (Aerobic)
        assert "Aerobic Respiration" in page.locator("#state-indicator").text_content()
        assert "36 ATP" in page.locator("#atp-output").text_content()
        assert "CO" in page.locator("#matter-outputs").text_content()
        assert "H2O" in page.locator("#matter-outputs").text_content()

        # 2. Change to high energy, but keep O2 high (Still Aerobic, but higher yield)
        page.evaluate("document.getElementById('energy-slider').value = '3'; window.updateSimulation();")
        page.wait_for_timeout(100)
        assert "Aerobic Respiration" in page.locator("#state-indicator").text_content()
        assert "108 ATP" in page.locator("#atp-output").text_content() # 3 * 36

        # 3. Drop O2 to 0 (Anaerobic)
        page.evaluate("document.getElementById('o2-slider').value = '0'; window.updateSimulation();")
        page.wait_for_timeout(100)
        assert "Anaerobic Fermentation" in page.locator("#state-indicator").text_content()
        assert "6 ATP" in page.locator("#atp-output").text_content() # 3 * 2
        assert "Lactic Acid" in page.locator("#matter-outputs").text_content()
        assert "CO" not in page.locator("#matter-outputs").text_content()

        # 4. Mixed State (High demand, medium O2)
        page.evaluate("document.getElementById('o2-slider').value = '40'; window.updateSimulation();")
        page.wait_for_timeout(100)
        assert "Mixed" in page.locator("#state-indicator").text_content()
        assert "Lactic Acid" in page.locator("#matter-outputs").text_content()
        assert "CO" in page.locator("#matter-outputs").text_content()

        # Take screenshot for verification
        os.makedirs('/home/jules/verification', exist_ok=True)
        page.screenshot(path='/home/jules/verification/aerobic_screenshot.png', full_page=True)

        browser.close()
        print("Aerobic vs Anaerobic simulation test passed.")

if __name__ == "__main__":
    test_aerobic_anaerobic()