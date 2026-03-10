import os
from playwright.sync_api import sync_playwright

def test_energy_change():
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'PhysicalSciences', 'EnergyChangeModel.html'))
    if not os.path.exists(html_path):
        html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'PhysicalScience', 'EnergyChangeModel.html'))

    file_uri = f"file://{html_path}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(file_uri, wait_until='networkidle')

        # Allow initial render
        page.wait_for_timeout(500)

        # 1. Test Initial State (Ek=100, Eg=-50, Eflow=0 => Et=-50)
        thermal_energy = page.evaluate("window.testingTools.getCalculatedThermalEnergy()")
        assert thermal_energy == -50, f"Expected initial thermal energy to be -50, got {thermal_energy}"

        # Test Chart Data matches
        chart_data = page.evaluate("window.testingTools.getChartData()")
        assert chart_data == [100, -50, -50, 0], f"Expected initial chart data [100, -50, -50, 0], got {chart_data}"

        # 2. Change Kinetic Energy (+300)
        page.evaluate("document.getElementById('ek-slider').value = 300;")
        page.evaluate("document.getElementById('ek-slider').dispatchEvent(new Event('input'))")

        # Ek=300, Eg=-50, Eflow=0 => Et = 0 - 300 - (-50) = -250
        thermal_energy = page.evaluate("window.testingTools.getCalculatedThermalEnergy()")
        assert thermal_energy == -250, f"Expected Et=-250 after Ek change, got {thermal_energy}"

        # 3. Change Energy Flow (+100)
        page.evaluate("document.getElementById('ef-slider').value = 100;")
        page.evaluate("document.getElementById('ef-slider').dispatchEvent(new Event('input'))")

        # Ek=300, Eg=-50, Eflow=100 => Et = 100 - 300 - (-50) = -150
        thermal_energy = page.evaluate("window.testingTools.getCalculatedThermalEnergy()")
        assert thermal_energy == -150, f"Expected Et=-150 after Eflow change, got {thermal_energy}"

        # Verify Chart Data update
        chart_data = page.evaluate("window.testingTools.getChartData()")
        assert chart_data == [300, -50, -150, 100], f"Expected chart [300, -50, -150, 100], got {chart_data}"

        # 4. Check that mathematical text updated correctly
        math_text = page.locator("#eq-step3").inner_text()
        assert "100" in math_text and "-150" in math_text, f"Expected math text to reflect calculation, got '{math_text}'"

        browser.close()

if __name__ == "__main__":
    test_energy_change()
    print("All tests passed for Energy Change Model.")