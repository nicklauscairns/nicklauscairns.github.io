import os
import json
from playwright.sync_api import sync_playwright

def test_lights_out():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = f"file://{os.path.abspath(os.path.join(script_dir, '..', 'Simulations', 'Logic', 'LightsOut.html'))}"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(file_path)

        # Ensure initial state is correct
        assert page.locator("#move-count").inner_text() == "0"

        # Override the random grid to a known state for testing
        # 1 means ON (true), 0 means OFF (false)
        known_grid = [
            [False, True,  False, False, False],
            [True,  True,  True,  False, False],
            [False, True,  False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False]
        ]

        # Set the grid state
        page.evaluate(f"window.setGrid({json.dumps(known_grid)});")

        # Verify initial rendering reflects known grid
        assert "light-on" in page.locator("#light-1-1").get_attribute("class")
        assert "light-on" in page.locator("#light-0-1").get_attribute("class")
        assert "light-off" in page.locator("#light-0-0").get_attribute("class")

        # Test toggling a light (click center light 1,1)
        # Expected: 1,1 toggles OFF, and neighbors (0,1; 2,1; 1,0; 1,2) toggle OFF
        page.evaluate("handleLightClick(1, 1)")

        assert page.locator("#move-count").inner_text() == "1"

        # Verify new state (all should be off now, which is a win)
        assert "light-off" in page.locator("#light-1-1").get_attribute("class")
        assert "light-off" in page.locator("#light-0-1").get_attribute("class")
        assert "light-off" in page.locator("#light-2-1").get_attribute("class")
        assert "light-off" in page.locator("#light-1-0").get_attribute("class")
        assert "light-off" in page.locator("#light-1-2").get_attribute("class")

        # Check win state
        assert page.locator("#win-message").is_visible(), "Win message should be visible on win"
        assert page.locator("#final-moves").inner_text() == "1"

        # Reset game
        page.evaluate("resetGame()")
        assert page.locator("#move-count").inner_text() == "0"
        assert not page.locator("#win-message").is_visible(), "Win message should hide on reset"

        # Verify it randomized to something not solved
        # We can't guarantee exactly what it is, but we know it's not solved because it forces an extra click if it is
        is_solved = page.evaluate("checkWinCondition()")
        assert not is_solved, "Game should not initialize in a solved state"

        browser.close()
        print("Lights Out tests passed!")

if __name__ == "__main__":
    test_lights_out()