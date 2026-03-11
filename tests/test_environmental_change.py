import os
from playwright.sync_api import sync_playwright

def test_environmental_change():
    """
    Tests the Environmental Change logic (NGSS HS-LS4-5).
    Verifies that a 'Drought' event causes the Specialist to go extinct
    and the Pest to increase in number.
    """

    # Resolve the file path dynamically based on the current script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = f"file://{os.path.join(script_dir, '..', 'Simulations', 'LifeSciences', 'EnvironmentalChangeExtinction.html')}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(file_path)

        # Ensure page is loaded
        page.wait_for_selector('canvas#populationChart')

        # Run for 2 "Years" to establish baseline
        page.evaluate("for(let i=0; i<2; i++) { window.updateSimulation(); }")

        baseline_state = page.evaluate("window.state")
        assert baseline_state['populations']['specialist'] > 0, "Specialist should exist."
        assert baseline_state['populations']['pest'] > 0, "Pest should exist."

        # Trigger Drought
        page.evaluate("window.triggerEvent('drought', 'Severe Drought')")

        # Run for 50 "Years" while Drought is active (simulate worst-case sustained event)
        # Note: In the UI, drought auto-recovers after 5 seconds, but we can manually sustain it for testing
        page.evaluate("""
            for(let i=0; i<50; i++) {
                window.state.activeEvent = 'drought';
                window.updateSimulation();
            }
        """)

        final_state = page.evaluate("window.state")

        # 1. Specialist (Amphibian) should go extinct due to low water quality
        assert final_state['populations']['specialist'] == 0, f"Specialist did not go extinct. Pop: {final_state['populations']['specialist']}"

        # 2. Pest (Insect) should increase due to less competition/predation and higher temp
        assert final_state['populations']['pest'] > baseline_state['populations']['pest'], "Pest population did not increase as expected during drought/stress."

        print("Playwright test passed: Environmental Events logic functions correctly.")
        browser.close()

if __name__ == "__main__":
    test_environmental_change()