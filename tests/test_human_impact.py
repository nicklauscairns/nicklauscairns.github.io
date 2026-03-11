from playwright.sync_api import sync_playwright
import os

def test_human_impact():
    possible_paths = [
        "Simulations/LifeSciences/HumanImpactBiodiversity.html",
        "../Simulations/LifeSciences/HumanImpactBiodiversity.html",
        "/app/Simulations/LifeSciences/HumanImpactBiodiversity.html"
    ]

    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = os.path.abspath(path)
            break

    if not file_path:
        raise FileNotFoundError("Could not find HumanImpactBiodiversity.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{file_path}", wait_until="networkidle")

        # 1. Verify Initial State (Perfect Biodiversity, Full Budget)
        assert "100 / 100" in page.locator("#val-biodiversity").text_content()
        assert "$10.0M" in page.locator("#val-budget").text_content()

        # 2. Apply Maximum Impacts
        page.locator("#btn-max-impact").click()
        page.wait_for_timeout(100)

        # Biodiversity should tank to near zero (Collapsing)
        status = page.locator("#status-label").text_content()
        assert "Collapsing" in status

        bio_text = page.locator("#val-biodiversity").text_content()
        # Should be around 18/100 based on formula
        bio_score = float(bio_text.split(" ")[0])
        assert bio_score < 30

        # 3. Apply Engineering Solutions (Spend Budget)
        # Add 3 levels of parks ($6M)
        page.evaluate("document.getElementById('sol-parks').value = '3'; document.getElementById('sol-parks').dispatchEvent(new Event('input'));")

        # Add 2 levels of water treatment ($3M)
        page.evaluate("document.getElementById('sol-water').value = '2'; document.getElementById('sol-water').dispatchEvent(new Event('input'));")

        page.wait_for_timeout(100)

        # Budget should be $1M remaining ($10 - $6 - $3)
        assert "$1.0M" in page.locator("#val-budget").text_content()

        # Biodiversity should have recovered significantly
        bio_text_recovered = page.locator("#val-biodiversity").text_content()
        bio_score_recovered = float(bio_text_recovered.split(" ")[0])
        assert bio_score_recovered > bio_score

        # 4. Try to overspend budget
        # Try to add 2 levels of Eradication ($2M) when only $1M is left
        page.evaluate("document.getElementById('sol-erad').value = '2'; document.getElementById('sol-erad').dispatchEvent(new Event('input'));")
        page.wait_for_timeout(100)

        # Budget should reject it and stay at $1M
        assert "$1.0M" in page.locator("#val-budget").text_content()

        # Value of slider should have reset to 0
        erad_val = page.evaluate("document.getElementById('sol-erad').value")
        assert erad_val == "0"

        # Take screenshot for verification
        os.makedirs('/home/jules/verification', exist_ok=True)
        page.screenshot(path='/home/jules/verification/human_impact_screenshot.png', full_page=True)

        browser.close()
        print("Human Impact & Biodiversity Solutions simulation test passed.")

if __name__ == "__main__":
    test_human_impact()