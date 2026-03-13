import os
from playwright.sync_api import Page, expect

def test_resonance_cascade(page: Page):
    file_path = "file://" + os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'Logic', 'ResonanceCascade.html'))

    # Block external resources
    page.route("**/*tailwindcss.com*", lambda route: route.abort())

    # Navigate
    page.goto(file_path)

    # Wait for initialization
    page.wait_for_timeout(500)

    # Get initial nodes
    nodes = page.evaluate("window.getNodes()")
    assert len(nodes) == 25

    # Check center node (index 12)
    initial_center_state = nodes[12]

    # Get neighbors based on center state
    neighbors = page.evaluate(f"window.getNeighbors(12, {initial_center_state})")

    # Cache initial states of neighbors
    initial_neighbor_states = {n: nodes[n] for n in neighbors}

    # Simulate a click on the center node
    page.evaluate("window.simulateClick(12)")

    new_nodes = page.evaluate("window.getNodes()")

    # Assert center node incremented
    assert new_nodes[12] == (initial_center_state + 1) % 4

    # Assert affected neighbors incremented
    for n in neighbors:
        assert new_nodes[n] == (initial_neighbor_states[n] + 1) % 4

    # The grid elements should exist
    grid_buttons = page.locator("#grid button")
    expect(grid_buttons).to_have_count(25)