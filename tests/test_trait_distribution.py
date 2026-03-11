from playwright.sync_api import sync_playwright
import os

def test_trait_distribution():
    possible_paths = [
        "Simulations/LifeSciences/TraitDistribution.html",
        "../Simulations/LifeSciences/TraitDistribution.html",
        "/app/Simulations/LifeSciences/TraitDistribution.html"
    ]

    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = os.path.abspath(path)
            break

    if not file_path:
        raise FileNotFoundError("Could not find TraitDistribution.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{file_path}", wait_until="networkidle")

        # 1. Verify Initial State (Mean 100, SD 15, Env 0)
        assert page.locator("#stat-mean").text_content() == "100.0 cm"
        assert page.locator("#stat-sd").text_content() == "15.0 cm"

        # Probability within 1 SD of a normal curve should be ~68%
        prob_text = page.locator("#stat-prob").text_content()
        prob_val = float(prob_text.replace("%", ""))
        assert 66.0 <= prob_val <= 70.0

        # 2. Modify Genetic Mean
        page.evaluate("document.getElementById('slider-genetic').value = '120'; window.updateSimulation();")
        page.wait_for_timeout(100)
        assert page.locator("#stat-mean").text_content() == "120.0 cm"

        # 3. Modify Environmental Factor
        page.evaluate("document.getElementById('slider-env').value = '-20'; window.updateSimulation();")
        page.wait_for_timeout(100)
        # New expressed mean should be Genetic (120) + Env (-20) = 100
        assert page.locator("#stat-mean").text_content() == "100.0 cm"

        # 4. Modify Variance
        page.evaluate("document.getElementById('slider-variance').value = '5'; window.updateSimulation();")
        page.wait_for_timeout(100)
        assert page.locator("#stat-sd").text_content() == "5.0 cm"

        # Take screenshot for verification
        os.makedirs('/home/jules/verification', exist_ok=True)
        page.screenshot(path='/home/jules/verification/trait_distribution_screenshot.png', full_page=True)

        browser.close()
        print("Trait Distribution simulation test passed.")

if __name__ == "__main__":
    test_trait_distribution()