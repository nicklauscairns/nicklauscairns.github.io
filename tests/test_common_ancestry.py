import os
from playwright.sync_api import sync_playwright

def test_common_ancestry_evidence():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', 'Simulations', 'LifeSciences', 'CommonAncestryEvidence.html')
    file_uri = f"file://{file_path}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(file_uri)

        # 1. Verify Initial UI State (Human vs Chimpanzee, DNA tab active)
        page.wait_for_selector("#species-a-select")

        # Verify DNA score for Human vs Chimp (should be high)
        page.wait_for_selector("#score-percent")
        score = page.locator("#score-percent").inner_text()
        assert "%" in score
        assert float(score.replace('%', '')) > 90, "Human vs Chimp DNA similarity should be > 90%"

        # 2. Change Species B to Mouse and verify DNA score drops
        page.select_option("#species-b-select", "mouse")
        page.wait_for_timeout(100) # give UI tiny bit to update
        mouse_score = page.locator("#score-percent").inner_text()
        assert float(mouse_score.replace('%', '')) < float(score.replace('%', '')), "Human vs Mouse DNA similarity should be lower than Human vs Chimp"

        # 3. Switch to Amino Acid Tab
        page.click("button[data-tab='amino']")
        page.wait_for_timeout(100)

        # Verify Amino Acid sequence displays
        assert page.locator("#tab-amino").is_visible()
        aa_score = page.locator("#score-percent").inner_text()
        assert "%" in aa_score

        # 4. Switch to Anatomy Tab
        page.click("button[data-tab='anatomy']")
        page.wait_for_timeout(100)

        # Verify Anatomy SVG displays and score changes to "Homologous Structure Match"
        assert page.locator("#tab-anatomy").is_visible()
        assert page.locator("#anat-svg-a svg").is_visible(), "Anatomy SVG A should be drawn"
        assert page.locator("#anat-svg-b svg").is_visible(), "Anatomy SVG B should be drawn"

        homology_text = page.locator("#score-percent").inner_text()
        assert homology_text == "Homologous Structure Match"

        # 5. Type into Evidence Log (testing SEP text area)
        log = page.locator("#analysis-log")
        log.fill("Testing the evidence log.")
        assert log.input_value() == "Testing the evidence log."

        browser.close()
        print("Common Ancestry Evidence simulation test passed.")

if __name__ == "__main__":
    test_common_ancestry_evidence()