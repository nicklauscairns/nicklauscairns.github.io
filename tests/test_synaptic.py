import os
from playwright.sync_api import Page, expect

def test_synaptic_links(page: Page):
    file_path = "file://" + os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'Logic', 'SynapticLinks.html'))

    page.route("**/*tailwindcss.com*", lambda route: route.abort())
    page.goto(file_path)
    page.wait_for_selector("#graphCanvas")

    # Output solution graph
    solution_graph = page.evaluate("window.getSolutionGraph()")

    # Override player graph to match solution exactly
    page.evaluate("(g) => window.setPlayerGraph(g)", solution_graph)

    # Trigger win check
    page.evaluate("window.checkWin()")

    is_solved_after = page.evaluate("window.isSolvedState()")
    assert is_solved_after is True
