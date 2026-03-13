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

    # Get nodes and partners
    nodes = page.evaluate("window.getNodes()")
    partners = page.evaluate("window.getPartners()")

    # Assert grid size is correct
    assert len(nodes) == 16
    assert len(partners) == 16

    # Assert every node has a partner and it's symmetrical
    for i in range(16):
        partner = partners[i]
        assert partners[partner] == i
        assert i != partner

    # Attempt a click on index 0 to test increment/decrement behavior
    initial_node_0_state = nodes[0]
    initial_partner_state = nodes[partners[0]]

    page.evaluate("window.simulateClick(0)")

    new_nodes = page.evaluate("window.getNodes()")
    assert new_nodes[0] == (initial_node_0_state + 1) % 4
    assert new_nodes[partners[0]] == (initial_partner_state - 1 + 4) % 4

    # The grid elements should exist
    grid_buttons = page.locator("#grid button")
    expect(grid_buttons).to_have_count(16)
