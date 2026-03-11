from playwright.sync_api import sync_playwright
import os

def test_mitosis():
    possible_paths = [
        "Simulations/LifeSciences/MitosisDifferentiation.html",
        "../Simulations/LifeSciences/MitosisDifferentiation.html",
        "/app/Simulations/LifeSciences/MitosisDifferentiation.html"
    ]

    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = os.path.abspath(path)
            break

    if not file_path:
        raise FileNotFoundError("Could not find MitosisDifferentiation.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{file_path}", wait_until="networkidle")

        # 1. Verify Initial State (Zygote)
        assert page.locator("#stat-count").text_content() == "1"
        assert "Zygote" in page.locator("#stage-title").text_content()
        assert "Identical" in page.locator("#stat-genetics").text_content()

        # 2. Advance Development to Cleavage
        page.locator("#btn-advance").click()
        page.wait_for_timeout(100)
        assert page.locator("#stat-count").text_content() == "8"
        assert "Cleavage" in page.locator("#stage-title").text_content()

        # 3. Advance to Gastrula (differentiation check)
        page.locator("#btn-advance").click() # Blastula
        page.wait_for_timeout(100)
        page.locator("#btn-advance").click() # Gastrula
        page.wait_for_timeout(100)
        assert page.locator("#stat-count").text_content() == "256"
        assert "Gastrulation" in page.locator("#stage-title").text_content()
        assert "Gene Expression Varies" in page.locator("#stat-genetics").text_content()

        # 4. Advance to Tissue (Final)
        page.locator("#btn-advance").click()
        page.wait_for_timeout(100)
        assert page.locator("#stat-count").text_content() == "1000+"
        assert "Specialized Tissues" in page.locator("#stage-title").text_content()

        # Advance button should be disabled
        is_disabled = page.evaluate("document.getElementById('btn-advance').disabled")
        assert is_disabled == True

        # 5. Reset check
        page.locator("#btn-reset").click()
        page.wait_for_timeout(100)
        assert page.locator("#stat-count").text_content() == "1"
        assert "Zygote" in page.locator("#stage-title").text_content()

        # Take screenshot for verification
        os.makedirs('/home/jules/verification', exist_ok=True)
        page.screenshot(path='/home/jules/verification/mitosis_screenshot.png', full_page=True)

        browser.close()
        print("Mitosis & Differentiation simulation test passed.")

if __name__ == "__main__":
    test_mitosis()