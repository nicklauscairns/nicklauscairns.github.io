import os
from playwright.sync_api import sync_playwright

def test_molecular_structures():
    # Use fallback paths to run robustly regardless of starting dir
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'PhysicalSciences', 'MolecularStructuresMaterials.html'))
    if not os.path.exists(html_path):
        html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'PhysicalScience', 'MolecularStructuresMaterials.html'))

    file_uri = f"file://{html_path}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(file_uri, wait_until='networkidle')

        # Ensure animation runs
        page.evaluate("document.hidden = false;")

        # Test default tab is Metals
        active_tab = page.evaluate("window.testingTools.getActiveTab()")
        assert active_tab == 'metals', f"Expected metals to be default tab, got {active_tab}"

        # Test Voltage Toggle in Metals
        btn_text = page.locator("#voltageToggleBtn").inner_text()
        assert "OFF" in btn_text
        page.locator("#voltageToggleBtn").click()
        btn_text = page.locator("#voltageToggleBtn").inner_text()
        assert "ON" in btn_text

        electrons = page.evaluate("window.testingTools.getElectrons()")
        assert len(electrons) > 0, "No electrons found in lattice"

        # Switch to Polymers
        page.locator("#tab-polymers").click()
        page.wait_for_timeout(100) # short wait for state update
        active_tab = page.evaluate("window.testingTools.getActiveTab()")
        assert active_tab == 'polymers', f"Expected polymers tab, got {active_tab}"

        # Test Polymer slider
        stress_val = page.evaluate("window.testingTools.getStressValue()")
        assert stress_val == 0.0, "Expected stress to be 0 initially"
        page.evaluate("document.getElementById('stressSlider').value = 50;")
        page.evaluate("document.getElementById('stressSlider').dispatchEvent(new Event('input'))")
        stress_val = page.evaluate("window.testingTools.getStressValue()")
        assert stress_val == 0.5, f"Expected stress to be 0.5, got {stress_val}"

        # Switch to Pharmaceuticals
        page.locator("#tab-pharma").click()
        page.wait_for_timeout(100)
        active_tab = page.evaluate("window.testingTools.getActiveTab()")
        assert active_tab == 'pharma', f"Expected pharma tab, got {active_tab}"

        # Test Drug C (Success)
        page.get_by_text("Test Drug C").click()
        status = page.evaluate("window.testingTools.getActiveDrugStatus()")
        assert status == 'dropping'

        # Wait for drop animation to complete
        page.wait_for_timeout(2500)

        status = page.evaluate("window.testingTools.getActiveDrugStatus()")
        assert status == 'docked', f"Drug C should have docked, but got {status}"
        status_text = page.locator("#pharmaStatus").inner_text()
        assert "Success" in status_text, f"Expected success message, got {status_text}"

        # Test Drug A (Failure)
        page.get_by_text("Test Drug A").click()
        page.wait_for_timeout(2500)
        status = page.evaluate("window.testingTools.getActiveDrugStatus()")
        assert status == 'rejected', f"Drug A should have rejected, but got {status}"
        status_text = page.locator("#pharmaStatus").inner_text()
        assert "Failure" in status_text, f"Expected failure message, got {status_text}"

        browser.close()

if __name__ == "__main__":
    test_molecular_structures()
    print("All tests passed for Molecular Structures & Designed Materials.")