import os
from playwright.sync_api import expect

def test_lyme_disease_ecology_rendering(page):
    """Test that the simulation loads and the chart canvas renders."""
    file_path = f"file://{os.path.abspath('Simulations/LifeSciences/LymeDiseaseEcology.html')}"

    # Intercept network to allow local files and required CDNs, blocking others
    page.route('**/*', lambda route: route.continue_() if route.request.url.startswith('file://') or any(kw in route.request.url for kw in ['tailwind', 'chart.js', 'cdn', 'unpkg']) else route.abort())

    page.goto(file_path)

    # Check that main title is visible
    expect(page.get_by_role("heading", name="Lyme Disease Ecological Cascade")).to_be_visible()

    # Check that the Chart.js canvas is present
    expect(page.locator("canvas#ecosystemChart")).to_be_visible()

def test_lyme_disease_ecology_interactions(page):
    """Test the interactions and state updates."""
    file_path = f"file://{os.path.abspath('Simulations/LifeSciences/LymeDiseaseEcology.html')}"

    page.route('**/*', lambda route: route.continue_() if route.request.url.startswith('file://') or any(kw in route.request.url for kw in ['tailwind', 'chart.js', 'cdn', 'unpkg']) else route.abort())
    page.goto(file_path)

    # Wait for state to initialize
    page.wait_for_function('window.simulationState !== undefined')

    # Test slider update
    page.evaluate("document.getElementById('foxPopulation').value = 10; document.getElementById('foxPopulation').dispatchEvent(new Event('input'));")
    fox_pop = page.evaluate("window.simulationState.foxPopulation")
    assert fox_pop == 0.1, f"Expected foxPopulation to be 0.1, got {fox_pop}"

    # Test button trigger
    trigger_btn = page.get_by_role("button", name="Trigger Oak Mast Year")
    trigger_btn.click()

    mast_triggered = page.evaluate("window.simulationState.oakMastTriggered")
    assert mast_triggered is True, "Expected oakMastTriggered to be True"

    # Wait for the simulation step to reset the oakMastTriggered flag (indicating it processed the mast)
    page.wait_for_function("window.simulationState.oakMastTriggered === false", timeout=5000)

    # If mast was triggered, acorns should spike in the step it processed it
    acorns = page.evaluate("window.simulationState.acorns")
    assert acorns > 100, f"Expected acorns to spike after mast, got {acorns}"