import os
from playwright.sync_api import sync_playwright

def test_field_energy():
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'PhysicalSciences', 'ElectricMagneticFieldEnergy.html'))
    file_uri = f"file://{html_path}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(file_uri, wait_until='networkidle')

        # Allow initial render
        page.evaluate("document.hidden = false;")
        page.wait_for_timeout(500)

        # 1. Test Initial State (Attractive)
        interaction = page.evaluate("window.testingTools.getInteraction()")
        assert interaction == 'electric_opp', f"Expected initial interaction 'electric_opp', got {interaction}"

        # Initial positions: obj1(150,200), obj2(450,200) -> dist = 300
        dist = page.evaluate("window.testingTools.getDist()")
        assert dist == 300, f"Expected initial dist 300, got {dist}"

        # Attractive: energy should be roughly (300-50)/450 = 250/450 = 0.55
        initial_energy = page.evaluate("window.testingTools.getStoredEnergy()")
        assert 0.5 < initial_energy < 0.6, f"Expected initial energy ~0.55, got {initial_energy}"

        initial_force = page.evaluate("window.testingTools.getForceMag()")

        # 2. Move objects closer
        page.evaluate("window.testingTools.moveObject2(250, 200);")
        page.wait_for_timeout(200) # let requestAnimationFrame update

        closer_dist = page.evaluate("window.testingTools.getDist()")
        assert closer_dist == 100, f"Expected closer dist 100, got {closer_dist}"

        closer_energy = page.evaluate("window.testingTools.getStoredEnergy()")
        assert closer_energy < initial_energy, f"Attractive objects moving closer should DECREASE stored energy. Was {initial_energy}, now {closer_energy}"

        closer_force = page.evaluate("window.testingTools.getForceMag()")
        assert closer_force > initial_force, f"Moving closer should INCREASE force. Was {initial_force}, now {closer_force}"

        # 3. Switch to Repulsive (same charges)
        page.evaluate("document.getElementById('interaction-type').value = 'electric_same';")
        page.evaluate("document.getElementById('interaction-type').dispatchEvent(new Event('change'))")
        page.wait_for_timeout(200)

        repulsive_interaction = page.evaluate("window.testingTools.getInteraction()")
        assert repulsive_interaction == 'electric_same', f"Expected interaction 'electric_same', got {repulsive_interaction}"

        repulsive_closer_energy = page.evaluate("window.testingTools.getStoredEnergy()")
        # Repulsive: energy is high when close
        assert repulsive_closer_energy > 0.8, f"Repulsive objects close together should have HIGH energy. Got {repulsive_closer_energy}"

        # 4. Move objects further apart
        page.evaluate("window.testingTools.moveObject2(500, 200);")
        page.wait_for_timeout(200)

        far_dist = page.evaluate("window.testingTools.getDist()")
        assert far_dist == 350, f"Expected far dist 350, got {far_dist}"

        far_energy = page.evaluate("window.testingTools.getStoredEnergy()")
        assert far_energy < repulsive_closer_energy, f"Repulsive objects moving apart should DECREASE energy. Was {repulsive_closer_energy}, now {far_energy}"

        browser.close()

if __name__ == "__main__":
    test_field_energy()
    print("All tests passed for Field Energy Model.")