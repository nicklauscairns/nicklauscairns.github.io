import os
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture
def simulation_page(page: Page) -> Page:
    """A fixture that navigates to the simulation page and sets up network routes."""
    # Build path relative to this test file location, not the current working directory
    file_path = f"file://{os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'LifeSciences', 'LymeDiseaseEcology.html'))}"

    # Intercept network to allow local files and chart.js CDN, but EXPLICITLY block tailwind to avoid timeouts
    def handle_route(route):
        url = route.request.url
        if url.startswith('file://') or 'chart.js' in url:
            route.continue_()
        else:
            route.abort()

    page.route('**/*', handle_route)
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

    # Wait for the simulation step to process the mast trigger
    simulation_page.wait_for_function("window.simulationState.oakMastTriggered === false", timeout=5000)

    # If mast was triggered, acorns should spike in the step it processed it
    acorns = simulation_page.evaluate("window.simulationState.acorns")
    assert acorns > 100, f"Expected acorns to spike after mast, got {acorns}"