import os
from playwright.sync_api import sync_playwright

def test_radiometric_dating():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Build absolute path to the local HTML file
        base_dir = "/app"
        file_path = f"file://{os.path.join(base_dir, 'Simulations/EarthSpaceSciences/RadiometricDatingExplorer.html')}"

        print(f"Navigating to {file_path}")
        page.goto(file_path, wait_until="networkidle")

        # 1. Verify UI Elements
        print("Verifying UI elements...")
        assert page.locator("#startBtn").is_visible(), "Start button should be visible"
        assert page.locator("#isotopeSelect").is_visible(), "Isotope select should be visible"
        assert page.locator("#rockCanvas").is_visible(), "Rock canvas should be visible"
        assert page.locator("#decayChart").is_visible(), "Decay chart should be visible"

        # 2. Verify Initial State
        print("Verifying initial state...")
        assert page.locator("#timeDisplay").inner_text() == "0.00", "Initial time should be 0.00"
        assert page.locator("#parentCount").inner_text() == "100.0%", "Initial parent count should be 100.0%"
        assert page.locator("#daughterCount").inner_text() == "0.0%", "Initial daughter count should be 0.0%"

        # 3. Run Simulation & Verify State Changes
        print("Running simulation...")
        # Make it fast
        slider = page.locator("#speedSlider")
        slider.fill("50")
        page.evaluate("document.getElementById('speedSlider').dispatchEvent(new Event('input'))")

        page.locator("#startBtn").click()

        # Wait a moment for decay to happen
        page.wait_for_timeout(1000)
        page.locator("#pauseBtn").click()

        # Time should have advanced
        current_time = float(page.locator("#timeDisplay").inner_text())
        assert current_time > 0, "Time should have advanced"

        # Parent count should be less than 100%
        parent_text = page.locator("#parentCount").inner_text().replace("%", "")
        current_parent = float(parent_text)
        assert current_parent < 100.0, "Parent count should have decreased"

        daughter_text = page.locator("#daughterCount").inner_text().replace("%", "")
        current_daughter = float(daughter_text)
        assert current_daughter > 0.0, "Daughter count should have increased"

        # 4. Verify Challenge Mode
        print("Verifying challenge mode...")
        page.locator("#generateUnknownBtn").click()
        assert page.locator("#challengeOverlay").is_visible(), "Challenge overlay should appear"

        # Guess incorrectly
        page.locator("#guessInput").fill("99999")
        page.locator("#submitGuessBtn").click()
        feedback = page.locator("#challengeFeedback").inner_text()
        assert "Incorrect" in feedback, "Should register incorrect guess"

        # Close challenge
        page.locator("#cancelChallengeBtn").click()
        assert not page.locator("#challengeOverlay").is_visible(), "Challenge overlay should be hidden"

        # Verify reset worked
        assert page.locator("#timeDisplay").inner_text() == "0.00", "Time should reset to 0.00"
        assert page.locator("#parentCount").inner_text() == "100.0%", "Parent count should reset to 100.0%"

        print("All Radiometric Dating tests passed!")
        browser.close()

if __name__ == "__main__":
    test_radiometric_dating()