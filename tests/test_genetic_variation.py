from playwright.sync_api import sync_playwright
import os

def test_genetic_variation():
    possible_paths = [
        "Simulations/LifeSciences/GeneticVariation.html",
        "../Simulations/LifeSciences/GeneticVariation.html",
        "/app/Simulations/LifeSciences/GeneticVariation.html"
    ]

    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = os.path.abspath(path)
            break

    if not file_path:
        raise FileNotFoundError("Could not find GeneticVariation.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{file_path}", wait_until="networkidle")

        # 1. Verify Initial State
        assert page.locator("#total-variations").text_content() == "0"

        # 2. Test Meiosis Module
        # Click the second segment of the first chromosome
        page.locator(".chromo-segment").nth(1).click()
        page.wait_for_timeout(100)

        # Verify count increased
        assert page.locator("#meiosis-count").text_content() == "1"
        assert page.locator("#total-variations").text_content() == "1"

        # Reset meiosis
        page.locator("#btn-reset-meiosis").click()

        # 3. Test Replication Errors Module
        # It's random, so we might need a few clicks to guarantee an error
        error_count = 0
        for _ in range(10):
            page.locator("#btn-replicate").click()
            page.wait_for_timeout(50)
            text_val = page.locator("#rep-error-count").text_content()
            error_count = int(text_val)
            if error_count > 0:
                break

        assert error_count > 0

        # 4. Test Environmental Mutations
        env_mut_count = 0
        for _ in range(10):
            # Click the bounding box
            page.locator("#env-box").click(position={"x": 50, "y": 50})
            page.wait_for_timeout(50)
            text_val = page.locator("#env-mut-count").text_content()
            env_mut_count = int(text_val)
            if env_mut_count > 0:
                break

        assert env_mut_count > 0

        # Total variations should reflect all modules
        total = int(page.locator("#total-variations").text_content())
        assert total == 1 + error_count + env_mut_count

        # Take screenshot for verification
        os.makedirs('/home/jules/verification', exist_ok=True)
        page.screenshot(path='/home/jules/verification/genetic_variation_screenshot.png', full_page=True)

        browser.close()
        print("Genetic Variation simulation test passed.")

if __name__ == "__main__":
    test_genetic_variation()