import os
from playwright.sync_api import sync_playwright

def test_natural_selection_adaptation():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', 'Simulations', 'LifeSciences', 'NaturalSelectionAdaptation.html')
    file_uri = f"file://{os.path.abspath(file_path)}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(file_uri)

        # Unhide document to allow requestAnimationFrame to run properly
        page.evaluate("Object.defineProperty(document, 'hidden', { value: false, writable: false });")

        # 1. Verify Initial UI State
        page.wait_for_selector("#btn-play")
        pop_text = page.locator("#stat-pop").inner_text()
        assert pop_text == "60", f"Expected initial population of 60, got {pop_text}"

        # 2. Start Simulation
        page.click("#btn-play")

        # Test Abiotic Factor: Drop temperature to -20 (Cold)
        # This should kill off thin-furred organisms rapidly
        page.evaluate("document.getElementById('rng-temp').value = '-20';")
        page.evaluate("document.getElementById('rng-temp').dispatchEvent(new Event('input'))")

        # Fast forward ticks
        page.evaluate("for(let i=0; i<100; i++) { window.updateSimulation(); }")

        # Wait to allow DOM update
        page.wait_for_timeout(200)

        # Population should have dropped (thin and med fur died)
        pop_text_after_cold = int(page.locator("#stat-pop").inner_text())
        assert pop_text_after_cold < 60, "Population should decrease when temperature drops to freezing"

        # Only thick fur (trait 2) should remain alive in extreme cold after some ticks
        thick_only = page.evaluate("""
            window.simState.organisms.every(org => org.furTrait === 2)
        """)
        # Give it a bit more time if they haven't all died yet
        if not thick_only:
             page.evaluate("for(let i=0; i<300; i++) { window.updateSimulation(); }")
             thick_only = page.evaluate("window.simState.organisms.every(org => org.furTrait === 2)")

        assert thick_only, "Only thick-furred organisms should survive extreme cold"

        # 3. Test Biotic Factor: Predator
        # Reset and run with predators
        page.click("#btn-reset")
        page.wait_for_timeout(100)
        page.evaluate("document.getElementById('chk-predator').click()")
        page.click("#btn-play")

        # Fast forward
        page.evaluate("for(let i=0; i<300; i++) { window.updateSimulation(); }")

        # Predators should eat something
        pop_text_after_pred = int(page.locator("#stat-pop").inner_text())
        assert pop_text_after_pred < 60, "Population should decrease due to predation"

        browser.close()
        print("Natural Selection Adaptation simulation test passed.")

if __name__ == "__main__":
    test_natural_selection_adaptation()
