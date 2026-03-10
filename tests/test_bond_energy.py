from playwright.sync_api import sync_playwright
import os
import time

def test_bond_energy():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        file_path = f"file://{os.path.abspath('Simulations/PhysicalSciences/BondEnergy.html')}"
        page.goto(file_path, wait_until="networkidle")

        # Verify initial state
        assert "Bond Energy Changes Simulator" in page.title()

        # Test Default (Combustion - Exothermic)
        assert page.is_enabled("#step1Btn")
        assert page.is_disabled("#step2Btn")

        page.click("#step1Btn")
        time.sleep(1) # wait for animation

        assert page.is_disabled("#step1Btn")
        assert page.is_enabled("#step2Btn")

        # Absorbed energy value should be positive
        absorbed = page.locator("#absorbedVal").inner_text()
        assert "+" in absorbed and "kJ" in absorbed

        page.click("#step2Btn")
        time.sleep(1)

        net_energy = page.locator("#netEnergyVal").inner_text()
        assert "-" in net_energy # Exothermic is negative net energy

        conclusion = page.locator("#conclusionText").inner_text()
        assert "Exothermic" in conclusion

        # Test Photosynthesis (Endothermic)
        page.click("input[value='photosynthesis']")
        time.sleep(0.5)

        page.click("#step1Btn")
        time.sleep(1)
        page.click("#step2Btn")
        time.sleep(1)

        net_energy = page.locator("#netEnergyVal").inner_text()
        assert "+" in net_energy # Endothermic is positive net energy

        conclusion = page.locator("#conclusionText").inner_text()
        assert "Endothermic" in conclusion

        print("Playwright test passed: BondEnergy logic functions correctly.")

        browser.close()

if __name__ == "__main__":
    test_bond_energy()