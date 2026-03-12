import os
from playwright.sync_api import sync_playwright

def test_towers_of_hanoi():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = f"file://{os.path.abspath(os.path.join(script_dir, '..', 'Simulations', 'Logic', 'TowersOfHanoi.html'))}"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(file_path)

        # Ensure initial state is correct (3 disks on first peg)
        disk_count = page.locator(".disk").count()
        assert disk_count == 3, f"Expected 3 disks initially, found {disk_count}"
        assert page.locator("#move-count").inner_text() == "0"

        # Test moving a disk: Peg 0 -> Peg 2
        page.evaluate("handlePegClick(0)") # Select disk on peg 0
        page.evaluate("handlePegClick(2)") # Move it to peg 2

        assert page.locator("#move-count").inner_text() == "1", "Move count should be 1"

        # Test invalid move: Trying to place larger disk on smaller disk
        # Disks are 3,2,1 on peg 0 initially.
        # After move 1, peg 0 has [3,2], peg 2 has [1]
        page.evaluate("handlePegClick(0)") # Select disk 2 on peg 0
        page.evaluate("handlePegClick(2)") # Try to move to peg 2 (invalid)

        # Deselect peg 0 which remained selected after the invalid move
        page.evaluate("handlePegClick(0)")

        # Move count should not increase
        assert page.locator("#move-count").inner_text() == "1", "Invalid move should not increase move count"

        # Complete a 3-disk game (optimal: 7 moves)
        # We are at move 1: Peg0 [3,2], Peg1 [], Peg2 [1]

        # Next move: peg 0 -> peg 1
        page.evaluate("handlePegClick(0)")
        page.evaluate("handlePegClick(1)") # Peg0 [3], Peg1 [2], Peg2 [1] (Moves: 2)

        # peg 2 -> peg 1
        page.evaluate("handlePegClick(2)")
        page.evaluate("handlePegClick(1)") # Peg0 [3], Peg1 [2,1], Peg2 [] (Moves: 3)

        # peg 0 -> peg 2
        page.evaluate("handlePegClick(0)")
        page.evaluate("handlePegClick(2)") # Peg0 [], Peg1 [2,1], Peg2 [3] (Moves: 4)

        # peg 1 -> peg 0
        page.evaluate("handlePegClick(1)")
        page.evaluate("handlePegClick(0)") # Peg0 [1], Peg1 [2], Peg2 [3] (Moves: 5)

        # peg 1 -> peg 2
        page.evaluate("handlePegClick(1)")
        page.evaluate("handlePegClick(2)") # Peg0 [1], Peg1 [], Peg2 [3,2] (Moves: 6)

        # peg 0 -> peg 2
        page.evaluate("handlePegClick(0)")
        page.evaluate("handlePegClick(2)") # Peg0 [], Peg1 [], Peg2 [3,2,1] (Moves: 7)

        assert page.locator("#move-count").inner_text() == "7", f"Move count should be 7, but was {page.locator('#move-count').inner_text()}"

        # Check win state
        assert page.locator("#win-message").is_visible(), "Win message should be visible"

        # Change disk count
        page.evaluate("document.getElementById('disk-count').value = '4'")
        page.evaluate("updateDiskCountLabel()")

        assert page.locator("#move-count").inner_text() == "0", "Move count should reset"
        assert not page.locator("#win-message").is_visible(), "Win message should be hidden on reset"
        assert page.locator(".disk").count() == 4, "Should have 4 disks now"

        browser.close()
        print("Towers of Hanoi tests passed!")

if __name__ == "__main__":
    test_towers_of_hanoi()