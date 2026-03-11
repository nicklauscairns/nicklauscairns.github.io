from playwright.sync_api import sync_playwright
import os

def test_dnatoprotein():
    # Use file path resolution that works locally and in testing environments
    possible_paths = [
        "Simulations/LifeSciences/DNAToProtein.html",
        "../Simulations/LifeSciences/DNAToProtein.html",
        "/app/Simulations/LifeSciences/DNAToProtein.html"
    ]

    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = os.path.abspath(path)
            break

    if not file_path:
        raise FileNotFoundError("Could not find DNAToProtein.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{file_path}", wait_until="networkidle")

        # 1. Verify default state (Muscle Protein)
        dna_bases = page.locator("#dna-coding .dna-base").all()
        assert len(dna_bases) == 12

        # Check initial structure and function text
        assert "Fibrous Rod" in page.locator("#structure-info").text_content()
        assert "Success: Rod structure enables muscle contraction" in page.locator("#function-info").text_content()

        # 2. Test toggling a DNA base (Mutation)
        # Change ATG -> TTG (Met -> Leu)
        # Base 0 is 'A'. Clicking it changes to 'T'
        # Note: We need to use page.evaluate because there's an overlay intercepting clicks
        page.evaluate("document.querySelectorAll('#dna-coding .dna-base')[0].click()")
        page.wait_for_timeout(100) # Small wait to allow UI update

        # Structure should change to truncated/misfold
        assert "Misfolded" in page.locator("#structure-info").text_content()

        # Function should fail
        assert "Fails:" in page.locator("#function-info").text_content()

        # 3. Test changing cell type environment
        page.locator('input[value="rbc"]').check()

        # 4. Test Evidence Logging
        # Log the misfolded state
        page.locator("#log-data-btn").click()

        log_entries = page.locator("#evidence-log-body tr").all()
        assert len(log_entries) == 1

        # Cell type column should be Red Blood Cell
        assert "Red Blood Cell" in log_entries[0].locator("td").nth(3).text_content()

        # 5. Test Presets
        page.locator("text='Hemoglobin (Normal)'").click()
        assert "Globular Bowl" in page.locator("#structure-info").text_content()
        assert "Success: Bowl structure carries oxygen" in page.locator("#function-info").text_content()

        # Verify cell type auto-switched to rbc
        assert page.locator('input[value="rbc"]').is_checked()

        # Take screenshot for verification
        os.makedirs('/home/jules/verification', exist_ok=True)
        page.screenshot(path='/home/jules/verification/dnatoprotein_screenshot.png', full_page=True)

        browser.close()
        print("DNAToProtein simulation test passed.")

if __name__ == "__main__":
    test_dnatoprotein()
