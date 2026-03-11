from playwright.sync_api import sync_playwright
import os

def test_macromolecules():
    possible_paths = [
        "Simulations/LifeSciences/Macromolecules.html",
        "../Simulations/LifeSciences/Macromolecules.html",
        "/app/Simulations/LifeSciences/Macromolecules.html"
    ]

    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = os.path.abspath(path)
            break

    if not file_path:
        raise FileNotFoundError("Could not find Macromolecules.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{file_path}", wait_until="networkidle")

        # 1. Verify Initial State
        assert page.locator("#inv-C").text_content() == "0"
        assert page.locator("#inv-H").text_content() == "0"
        assert page.locator("#inv-O").text_content() == "0"
        assert page.locator("#inv-N").text_content() == "0"

        # Synthesis button should be disabled initially
        is_disabled = page.evaluate("document.getElementById('btn-synthesize').disabled")
        assert is_disabled == True

        # 2. Breakdown Sugar
        page.locator("#btn-breakdown").click()
        page.wait_for_timeout(100)

        # Check new inventory
        assert page.locator("#inv-C").text_content() == "6"
        assert page.locator("#inv-H").text_content() == "12"
        assert page.locator("#inv-O").text_content() == "6"
        assert page.locator("#inv-N").text_content() == "0" # Still 0 N

        # Synthesis button should still be disabled for Glycine (requires N)
        is_disabled = page.evaluate("document.getElementById('btn-synthesize').disabled")
        assert is_disabled == True

        # 3. Add Nitrogen
        page.evaluate("adjustInventory('N', 1)")
        page.wait_for_timeout(100)
        assert page.locator("#inv-N").text_content() == "1"

        # Now synthesis should be available
        is_disabled = page.evaluate("document.getElementById('btn-synthesize').disabled")
        assert is_disabled == False

        # 4. Synthesize Molecule (Glycine: C2H5NO2)
        page.locator("#btn-synthesize").click()
        page.wait_for_timeout(100)

        # Check inventory deductions (6-2=4, 12-5=7, 6-2=4, 1-1=0)
        assert page.locator("#inv-C").text_content() == "4"
        assert page.locator("#inv-H").text_content() == "7"
        assert page.locator("#inv-O").text_content() == "4"
        assert page.locator("#inv-N").text_content() == "0"

        # Check product rendered
        product_count = page.locator(".product-item").count()
        assert product_count == 1
        assert "Glycine" in page.locator(".product-item").first.text_content()

        # Take screenshot for verification
        os.makedirs('/home/jules/verification', exist_ok=True)
        page.screenshot(path='/home/jules/verification/macromolecules_screenshot.png', full_page=True)

        browser.close()
        print("Macromolecules simulation test passed.")

if __name__ == "__main__":
    test_macromolecules()