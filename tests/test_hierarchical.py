from playwright.sync_api import sync_playwright
import os

def test_hierarchical():
    possible_paths = [
        "Simulations/LifeSciences/HierarchicalOrganization.html",
        "../Simulations/LifeSciences/HierarchicalOrganization.html",
        "/app/Simulations/LifeSciences/HierarchicalOrganization.html"
    ]

    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = os.path.abspath(path)
            break

    if not file_path:
        raise FileNotFoundError("Could not find HierarchicalOrganization.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{file_path}", wait_until="networkidle")

        # 1. Verify Initial State (Digestive System, Level 1)
        assert "Enterocyte" in page.locator("#info-title").text_content()
        assert "Level 1: Cell" in page.locator("#info-level-name").text_content()
        assert "Microscopic (10µm)" in page.locator("#scale-indicator").text_content()

        # 2. Test Level Navigation (Digestive System)
        # Click Level 3 (Organ)
        page.evaluate("document.querySelectorAll('.level-btn')[2].click()")
        page.wait_for_timeout(100) # Wait for UI update

        assert "Small Intestine" in page.locator("#info-title").text_content()
        assert "Level 3: Organ" in page.locator("#info-level-name").text_content()

        # Click Level 5 (Organism)
        page.evaluate("document.querySelectorAll('.level-btn')[4].click()")
        page.wait_for_timeout(100)
        assert "Human Body" in page.locator("#info-title").text_content()

        # 3. Test System Switch (to Respiratory)
        page.evaluate("document.querySelectorAll('.system-btn')[1].click()")
        page.wait_for_timeout(100)

        # Should reset to level 1 for Respiratory System
        assert "Type I Pneumocyte" in page.locator("#info-title").text_content()
        assert "Level 1: Cell" in page.locator("#info-level-name").text_content()

        # Test Respiratory Level 4 (Organ System)
        page.evaluate("document.querySelectorAll('.level-btn')[3].click()")
        page.wait_for_timeout(100)
        assert "Respiratory System" in page.locator("#info-title").text_content()
        assert "ventilation (breathing)" in page.locator("#info-function").text_content()

        # Take screenshot for verification
        os.makedirs('/home/jules/verification', exist_ok=True)
        page.screenshot(path='/home/jules/verification/hierarchical_screenshot.png', full_page=True)

        browser.close()
        print("Hierarchical Organization simulation test passed.")

if __name__ == "__main__":
    test_hierarchical()