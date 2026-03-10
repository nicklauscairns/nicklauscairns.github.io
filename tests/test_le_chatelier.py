from playwright.sync_api import sync_playwright
import os
import time

def test_le_chatelier():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        file_path = f"file://{os.path.abspath('Simulations/PhysicalSciences/LeChatelier.html')}"
        page.goto(file_path, wait_until="networkidle")

        # Verify initial state
        assert "Le Chatelier's Principle Simulator" in page.title()

        # Test add reactant (N2) -> shifts right
        page.click("#addN2Btn")
        time.sleep(1) # Wait for UI update and shift

        # Verify explanation text updated
        explanation = page.locator("#explanationText").inner_text()
        assert "Adding a reactant" in explanation

        # Verify shift indicator
        # Using evaluate because the class opacity transition might be tricky to catch with exact timing
        indicator_text = page.locator("#shiftIndicator").inner_text()
        assert "Right" in indicator_text

        # Test decrease volume (increase pressure) -> shifts right (fewer moles)
        page.evaluate("document.getElementById('volumeSlider').value = 50")
        page.locator("#volumeSlider").dispatch_event("change")
        time.sleep(1)

        explanation = page.locator("#explanationText").inner_text()
        assert "Decreasing volume" in explanation
        assert "right" in explanation

        # Test increase temp -> shifts left (endothermic direction)
        page.evaluate("document.getElementById('tempSlider').value = 800")
        page.locator("#tempSlider").dispatch_event("change")
        time.sleep(1)

        explanation = page.locator("#explanationText").inner_text()
        assert "Increasing temperature" in explanation
        assert "left" in explanation

        print("Playwright test passed: LeChatelier logic functions correctly.")

        browser.close()

if __name__ == "__main__":
    test_le_chatelier()