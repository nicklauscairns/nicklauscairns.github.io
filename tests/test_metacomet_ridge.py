import os
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture
def sim_page(page: Page):
    """Fixture to load the simulation page with route interception."""
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'EarthSpaceSciences', 'MetacometRidgeFormation.html'))
    file_url = f"file://{file_path}"

    # Intercept network requests to allow local files and Tailwind CDN, block others
    def handle_route(route):
        url = route.request.url
        if url.startswith("file://") or "tailwindcss.com" in url or "googletagmanager" in url:
            route.continue_()
        else:
            route.abort()

    page.route("**/*", handle_route)
    page.goto(file_url)

    # Override document.hidden for requestAnimationFrame
    page.evaluate("Object.defineProperty(document, 'hidden', { value: false, writable: false });")

    return page

def get_state(page: Page):
    """Helper to get the current simulation state."""
    return page.evaluate("window.simulationState")

def test_initial_state(sim_page: Page):
    """Test the initial state of the simulation."""
    state = get_state(sim_page)
    assert state['stage'] == 0
    assert state['riftWidth'] == 0
    assert state['animating'] is False

def test_rifting_stage(sim_page: Page):
    """Test that clicking the Rifting button advances the stage and updates state."""
    sim_page.click("#btn-rift")

    # Wait for the animation to finish (stage advances internally or animating becomes false)
    sim_page.wait_for_function("window.simulationState.animating === false")

    state = get_state(sim_page)
    assert state['stage'] == 1
    assert state['riftWidth'] >= 250
    assert state['valleyDrop'] >= 100

    # Ensure next button is enabled
    is_disabled = sim_page.evaluate("document.getElementById('btn-sediment').disabled")
    assert not is_disabled

def test_full_sequence(sim_page: Page):
    """Test the complete sequence of geological events."""
    # 1. Rifting
    sim_page.click("#btn-rift")
    sim_page.wait_for_function("window.simulationState.animating === false")

    # 2. Sedimentation
    sim_page.click("#btn-sediment")
    sim_page.wait_for_function("window.simulationState.animating === false")
    state = get_state(sim_page)
    assert state['stage'] == 2
    assert state['sedimentDepth'] >= 60

    # 3. Volcanism
    sim_page.click("#btn-volcano")
    sim_page.wait_for_function("window.simulationState.animating === false")
    state = get_state(sim_page)
    assert state['stage'] == 3
    assert state['basaltDepth'] >= 30

    # 4. Tilting
    sim_page.click("#btn-tilt")
    sim_page.wait_for_function("window.simulationState.animating === false")
    state = get_state(sim_page)
    assert state['stage'] == 4
    assert state['tiltAngle'] >= 15

    # 5. Erosion
    sim_page.click("#btn-erode")
    sim_page.wait_for_function("window.simulationState.animating === false")
    state = get_state(sim_page)
    assert state['stage'] == 5
    assert state['erosionLevel'] >= 70

    # Observation panel should be visible
    is_hidden = sim_page.evaluate("document.getElementById('observation-panel').classList.contains('hidden')")
    assert not is_hidden

def test_reset(sim_page: Page):
    """Test the reset functionality."""
    # Advance state
    sim_page.click("#btn-rift")
    sim_page.wait_for_function("window.simulationState.animating === false")

    # Reset
    sim_page.click("#btn-reset")

    state = get_state(sim_page)
    assert state['stage'] == 0
    assert state['riftWidth'] == 0
    assert state['valleyDrop'] == 0
    assert state['animating'] is False
