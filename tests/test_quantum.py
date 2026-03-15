import os
from playwright.sync_api import Page, expect

def test_quantum_entanglement(page: Page):
    # Determine the local file path dynamically
    file_path = "file://" + os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'Logic', 'QuantumEntanglement.html'))

    # Block external resources for speed
    page.route("**/*tailwindcss.com*", lambda route: route.abort())

    # Navigate directly to the file
    page.goto(file_path)

    # Allow scripts to initialize
    page.wait_for_selector("#grid button")

    # Get initial nodes
    nodes = page.evaluate("window.getNodes()")

    # Assert grid size is correct
    assert len(nodes) == 16

    # Attempt a click on index 5 (row 1, col 1) to test increment/decrement behavior
    target = 5
    page.evaluate(f"window.simulateClick({target})")

    new_nodes = page.evaluate("window.getNodes()")

    # Target should be incremented (modulo 4)
    expected_target = (nodes[target] + 1) % 4
    assert new_nodes[target] == expected_target

    # Neighbors should be decremented (modulo 4)
    COLS = 4
    row, col = divmod(target, COLS)
    neighbors = []
    if row > 0: neighbors.append(target - COLS)
    if row < COLS - 1: neighbors.append(target + COLS)
    if col > 0: neighbors.append(target - 1)
    if col < COLS - 1: neighbors.append(target + 1)

    for n in neighbors:
        expected = (nodes[n] - 1 + 4) % 4
        assert new_nodes[n] == expected

    # Non-neighbors should be unchanged
    for i in range(16):
        if i not in neighbors and i != target:
            assert new_nodes[i] == nodes[i]

    # The grid elements should exist
    grid_buttons = page.locator("#grid button")
    expect(grid_buttons).to_have_count(16)
