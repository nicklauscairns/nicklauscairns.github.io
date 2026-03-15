import os
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture
def simulation_page(page: Page) -> Page:
    """A fixture that navigates to the simulation page and sets up network routes."""
    file_path = f"file://{os.path.abspath('Simulations/LifeSciences/LymeDiseaseEcology.html')}"
    # Intercept network to allow local files and required CDNs, blocking others
    page.route('**/*', lambda route: route.continue_() if route.request.url.startswith('file://') or any(kw in route.request.url for kw in ['tailwind', 'chart.js', 'cdn', 'unpkg']) else route.abort())
    page.goto(file_path)
    return page

def test_lyme_disease_ecology_rendering(simulation_page: Page):
    """Test that the simulation loads and the chart canvas renders."""
    # Check that main title is visible
    expect(simulation_page.get_by_role("heading", name="Lyme Disease Ecological Cascade")).to_be_visible()

    # Check that the Chart.js canvas is present
    expect(simulation_page.locator("canvas#ecosystemChart")).to_be_visible()

def test_lyme_disease_ecology_interactions(simulation_page: Page):
    """Test the interactions and state updates."""
    # Wait for state to initialize
    simulation_page.wait_for_function('window.simulationState !== undefined')

    # Test slider update
    simulation_page.evaluate("document.getElementById('foxPopulation').value = 10; document.getElementById('foxPopulation').dispatchEvent(new Event('input'));")
    fox_pop = simulation_page.evaluate("window.simulationState.foxPopulation")
    assert fox_pop == 0.1, f"Expected foxPopulation to be 0.1, got {fox_pop}"

    # Test button trigger
    trigger_btn = simulation_page.get_by_role("button", name="Trigger Oak Mast Year")
    trigger_btn.click()

    mast_triggered = simulation_page.evaluate("window.simulationState.oakMastTriggered")
    assert mast_triggered is True, "Expected oakMastTriggered to be True"

    # Wait for the simulation step to reset the oakMastTriggered flag (indicating it processed the mast)
    simulation_page.wait_for_function("window.simulationState.oakMastTriggered === false", timeout=5000)

    # If mast was triggered, acorns should spike in the step it processed it
    acorns = simulation_page.evaluate("window.simulationState.acorns")
    assert acorns > 100, f"Expected acorns to spike after mast, got {acorns}"