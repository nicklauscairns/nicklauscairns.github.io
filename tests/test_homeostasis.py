from playwright.sync_api import sync_playwright
import os
import math

def test_homeostasis():
    possible_paths = [
        "Simulations/LifeSciences/Homeostasis.html",
        "../Simulations/LifeSciences/Homeostasis.html",
        "/app/Simulations/LifeSciences/Homeostasis.html"
    ]

    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = os.path.abspath(path)
            break

    if not file_path:
        raise FileNotFoundError("Could not find Homeostasis.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{file_path}", wait_until="networkidle")

        # 1. Verify Initial State
        assert page.locator("#core-temp-val").text_content().strip() == "37.0 °C"
        assert "60 bpm" in page.locator("#hr-val").text_content()
        assert "Stable" in page.locator("#status-val").text_content()

        # 2. Test Simulation Controls and Data Logging (Running for a few ticks)
        page.locator("button[data-level='running']").click()
        page.locator("#btn-play").click()

        # Wait for 3 simulation ticks (3 real-time seconds)
        page.wait_for_timeout(3500)

        # Pause sim
        page.locator("#btn-play").click()

        # Verify time advanced
        sim_time = page.locator("#sim-time").text_content()
        assert sim_time != "00:00"

        # Heart rate should have increased (target is 160, starts at 60)
        hr_text = page.locator("#hr-val").text_content()
        current_hr = int(hr_text.split(" ")[0])
        assert current_hr > 60

        # Data log should have entries
        log_rows = page.locator("#data-log tr").count()
        assert log_rows >= 3

        # 3. Test Reset
        page.locator("#btn-reset").click()
        assert page.locator("#sim-time").text_content() == "00:00"
        assert page.locator("#core-temp-val").text_content().strip() == "37.0 °C"
        assert "60 bpm" in page.locator("#hr-val").text_content()
        assert page.locator("#data-log tr").count() == 1 # Initial state logs once on reset

        # Take screenshot for verification
        os.makedirs('/home/jules/verification', exist_ok=True)
        page.screenshot(path='/home/jules/verification/homeostasis_screenshot.png', full_page=True)

        browser.close()
        print("Homeostasis simulation test passed.")

if __name__ == "__main__":
    test_homeostasis()