from playwright.sync_api import sync_playwright
import os

def test_trophic():
    possible_paths = [
        "Simulations/LifeSciences/TrophicEnergy.html",
        "../Simulations/LifeSciences/TrophicEnergy.html",
        "/app/Simulations/LifeSciences/TrophicEnergy.html"
    ]

    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = os.path.abspath(path)
            break

    if not file_path:
        raise FileNotFoundError("Could not find TrophicEnergy.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{file_path}", wait_until="networkidle")

        # 1. Verify Initial State (10,000 J at 10%)
        assert page.locator("#producer-energy-val").text_content() == "10,000 J"
        assert page.locator("#efficiency-val").text_content() == "10%"

        # Check Pyramid rendering
        levels = page.locator(".trophic-level").all()
        assert len(levels) == 4

        # Check data table mathematical accuracy (Level 1 should have 10k J)
        rows = page.locator("#data-table tr").all()
        assert "10,000" in rows[0].locator("td").nth(1).text_content() # Energy available
        assert "9,000" in rows[0].locator("td").nth(2).text_content() # Heat loss

        # Level 2 should have 10% of 10k = 1k
        assert "1,000" in rows[1].locator("td").nth(1).text_content()

        # 2. Adjust Efficiency to 20%
        page.evaluate("document.getElementById('efficiency').value = '20'; window.updateModel();")
        page.wait_for_timeout(100)
        assert page.locator("#efficiency-val").text_content() == "20%"

        # Re-check Level 2, should now be 20% of 10k = 2k
        rows = page.locator("#data-table tr").all()
        assert "2,000" in rows[1].locator("td").nth(1).text_content()

        # Take screenshot for verification
        os.makedirs('/home/jules/verification', exist_ok=True)
        page.screenshot(path='/home/jules/verification/trophic_screenshot.png', full_page=True)

        browser.close()
        print("Trophic Energy simulation test passed.")

if __name__ == "__main__":
    test_trophic()