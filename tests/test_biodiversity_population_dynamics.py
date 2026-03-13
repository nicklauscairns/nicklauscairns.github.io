import os
from playwright.sync_api import sync_playwright


def test_biodiversity_population_dynamics():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(
        current_dir, '..', 'Simulations', 'LifeSciences', 'BiodiversityPopulationDynamics.html'
    )
    file_uri = f"file://{file_path}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(file_uri)

        page.wait_for_selector('#ecoChart')
        page.wait_for_selector('#populationOut')

        baseline = int(page.locator('#populationOut').inner_text())
        base_b = float(page.locator('#biodiversityOut').inner_text())

        page.evaluate("""
            const setAndDispatch = (id, value) => {
              const el = document.getElementById(id);
              el.value = value;
              el.dispatchEvent(new Event('input'));
            };
            setAndDispatch('pollution', 60);
            setAndDispatch('climateStress', 55);
            setAndDispatch('invasive', 50);
            document.getElementById('runBtn').click();
        """)
        page.wait_for_timeout(250)

        stressed = int(page.locator('#populationOut').inner_text())
        stressed_b = float(page.locator('#biodiversityOut').inner_text())

        assert stressed < baseline, 'Higher stress should reduce final population'
        assert stressed_b < base_b, 'Higher stress should reduce biodiversity index'

        page.click('#disturbanceBtn')
        page.wait_for_timeout(250)
        disturbed = int(page.locator('#populationOut').inner_text())
        disturbed_b = float(page.locator('#biodiversityOut').inner_text())

        assert disturbed <= stressed, 'Disturbance should not improve stressed population'
        assert disturbed_b <= stressed_b, 'Disturbance should not improve stressed biodiversity'

        # Evidence table should now contain disturbed values and negative deltas.
        delta_pop = int(page.locator('#deltaPop').inner_text())
        delta_bio = float(page.locator('#deltaBio').inner_text())
        assert delta_pop <= 0
        assert delta_bio <= 0

        # Verify exposed pure functions
        k_low = page.evaluate("window.calculateK(500, 10, 10, 10, 'regional')")
        k_high = page.evaluate("window.calculateK(500, 60, 60, 60, 'regional')")
        assert k_low > k_high, 'Carrying capacity should decline with higher stress inputs'

        k_global = page.evaluate("window.calculateK(500, 10, 10, 10, 'global')")
        k_local = page.evaluate("window.calculateK(500, 10, 10, 10, 'local')")
        assert k_global > k_local, 'Scale should affect carrying capacity'

        risk = page.evaluate('window.identifyDominantRisk(10, 55, 35)')
        assert risk == 'Climate stress'

        result = page.evaluate("window.runModel({area:500,pollution:20,climate:15,invasive:10,scale:'regional'})")
        assert len(result['years']) == 31
        assert len(result['population']) == 31
        assert len(result['biodiversity']) == 31

        browser.close()


if __name__ == '__main__':
    test_biodiversity_population_dynamics()
