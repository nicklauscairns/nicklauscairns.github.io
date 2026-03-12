import os
from playwright.sync_api import sync_playwright

def test_mastermind():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = f"file://{os.path.abspath(os.path.join(script_dir, '..', 'Simulations', 'Logic', 'Mastermind.html'))}"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(file_path)

        # Ensure initial state is correct
        assert page.locator("#attempt-count").inner_text() == "0"

        # Override the random secret code to a known state for testing
        page.evaluate("window.setSecretCode(['red', 'blue', 'green', 'yellow']);")

        # Select colors and place them in the first row (Attempt 0)
        page.evaluate("selectColor('red')")
        page.evaluate("placePeg(0)")

        page.evaluate("selectColor('red')") # Intentional duplicate guess
        page.evaluate("placePeg(1)")

        page.evaluate("selectColor('green')")
        page.evaluate("placePeg(2)")

        page.evaluate("selectColor('orange')")
        page.evaluate("placePeg(3)")

        # Check guess (Expected feedback: 2 black (red@0, green@2), 0 white)
        page.evaluate("checkGuess()")

        assert page.locator("#attempt-count").inner_text() == "1"

        # Check feedback visually (we placed black classes)
        # We need to evaluate JS to check classes because Playwright locators might be tricky with multiple elements
        feedback_classes = page.evaluate("Array.from(document.getElementById('feedback-0').children).map(c => c.className)")

        # Should have exactly two 'feedback-black' classes
        black_count = sum(1 for c in feedback_classes if 'feedback-black' in c)
        white_count = sum(1 for c in feedback_classes if 'feedback-white' in c)

        assert black_count == 2, f"Expected 2 black pegs, got {black_count}"
        assert white_count == 0, f"Expected 0 white pegs, got {white_count}"

        # Attempt 1: All correct colors, wrong positions
        page.evaluate("selectColor('yellow')")
        page.evaluate("placePeg(0)")

        page.evaluate("selectColor('green')")
        page.evaluate("placePeg(1)")

        page.evaluate("selectColor('blue')")
        page.evaluate("placePeg(2)")

        page.evaluate("selectColor('red')")
        page.evaluate("placePeg(3)")

        page.evaluate("checkGuess()")

        assert page.locator("#attempt-count").inner_text() == "2"

        feedback_classes_1 = page.evaluate("Array.from(document.getElementById('feedback-1').children).map(c => c.className)")
        white_count_1 = sum(1 for c in feedback_classes_1 if 'feedback-white' in c)
        assert white_count_1 == 4, f"Expected 4 white pegs, got {white_count_1}"

        # Attempt 2: Win condition
        page.evaluate("selectColor('red')")
        page.evaluate("placePeg(0)")

        page.evaluate("selectColor('blue')")
        page.evaluate("placePeg(1)")

        page.evaluate("selectColor('green')")
        page.evaluate("placePeg(2)")

        page.evaluate("selectColor('yellow')")
        page.evaluate("placePeg(3)")

        page.evaluate("checkGuess()")

        assert page.locator("#attempt-count").inner_text() == "3"

        assert page.locator("#end-message").is_visible(), "End message should be visible on win"
        assert "Code Broken" in page.locator("#end-message").inner_text(), "Should say code broken"

        # Reset game
        page.evaluate("resetGame()")
        assert page.locator("#attempt-count").inner_text() == "0"
        assert not page.locator("#end-message").is_visible(), "End message should hide on reset"

        browser.close()
        print("Mastermind tests passed!")

if __name__ == "__main__":
    test_mastermind()