import os
from playwright.sync_api import sync_playwright

def test_habitat_fragmentation():
    """
    Tests the Habitat Fragmentation Mitigation logic (NGSS HS-LS4-6).
    Verifies that 'Do Nothing' leads to low genetic diversity and population decline,
    while 'Wildlife Overpass' mitigates the decline.
    """

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = f"file://{os.path.join(script_dir, '..', 'Simulations', 'LifeSciences', 'HabitatFragmentationMitigation.html')}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # Test 1: Baseline (Do Nothing) - should lead to decline
        page = browser.new_page()
        page.goto(file_path)
        page.wait_for_selector('canvas#popChart')

        # Run for 50 years with baseline (connectivity 0) to allow significant decay
        page.evaluate("""
            window.state.isRunning = true;
            for(let i=0; i<50; i++) { window.runSimulationStep(); }
        """)
        baseline_state = page.evaluate("window.state")

        # Population and genetics should be significantly lower than starting (50 and 0.95)
        assert baseline_state['west']['pop'] < 45, f"Baseline population should decline due to inbreeding. Was: {baseline_state['west']['pop']}"
        assert baseline_state['west']['genetics'] < 0.8, "Baseline genetic diversity should decay."

        # Test 2: Overpass Solution - should stabilize
        page2 = browser.new_page()
        page2.goto(file_path)
        page2.wait_for_selector('canvas#popChart')

        # Select Overpass and run for 50 years
        page2.evaluate("""
            window.state.solution = 'overpass';
            window.state.isRunning = true;
            for(let i=0; i<50; i++) { window.runSimulationStep(); }
        """)
        overpass_state = page2.evaluate("window.state")

        # Population and genetics should be higher than baseline scenario
        assert overpass_state['west']['pop'] > baseline_state['west']['pop'], "Overpass should result in higher population than baseline."
        assert overpass_state['west']['genetics'] > baseline_state['west']['genetics'], "Overpass should result in higher genetic diversity than baseline."

        print("Playwright test passed: Habitat Fragmentation Mitigation logic functions correctly.")
        browser.close()

if __name__ == "__main__":
    test_habitat_fragmentation()