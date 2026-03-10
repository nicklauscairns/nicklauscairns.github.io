from playwright.sync_api import sync_playwright
import os
import time

def test_conservation_of_mass():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        file_path = f"file://{os.path.abspath('Simulations/PhysicalSciences/ConservationOfMass.html')}"
        page.goto(file_path, wait_until="networkidle")

        # Verify initial state
        assert "Conservation of Mass" in page.title()

        # Select Water
        page.select_option("#reactionSelect", "water")

        # Unbalanced check
        page.click("#checkBtn")
        assert "Not Balanced yet" in page.locator("#feedbackMsg").inner_text()

        # Balance the equation: 2 H2 + 1 O2 -> 2 H2O
        page.fill("input[data-id='r1']", "2")
        page.fill("input[data-id='p1']", "2")

        # Ensure scale update propagates
        time.sleep(0.5)

        page.click("#checkBtn")
        assert "Equation is Balanced" in page.locator("#feedbackMsg").inner_text()

        # Verify mass calculations
        left_mass = page.locator("#leftMass").inner_text()
        right_mass = page.locator("#rightMass").inner_text()
        assert left_mass == "36" # (2 * 2*1) + (1 * 2*16) = 4 + 32 = 36
        assert right_mass == "36" # (2 * (2*1 + 16)) = 36

        # Select Methane
        page.select_option("#reactionSelect", "methane")
        page.fill("input[data-id='r2']", "2")
        page.fill("input[data-id='p2']", "2")
        time.sleep(0.5)
        page.click("#checkBtn")
        assert "Equation is Balanced" in page.locator("#feedbackMsg").inner_text()

        print("Playwright test passed: ConservationOfMass logic functions correctly.")

        browser.close()

if __name__ == "__main__":
    test_conservation_of_mass()