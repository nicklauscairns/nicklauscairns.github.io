import re
import pytest
from playwright.sync_api import Page, expect
import os

@pytest.fixture
def sim_url():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "Simulations", "EarthSpaceSciences", "HartfordBasinGeology.html")
    return f"file://{file_path}"

def test_initial_state_and_rendering(page: Page, sim_url: str):
    page.route('**/*', lambda route: route.continue_() if route.request.url.startswith('file://') or any(kw in route.request.url for kw in ['tailwindcss.com', 'unpkg', 'cdn', 'cloudflare', 'fonts']) else route.abort())
    page.goto(sim_url)

    # Verify Title and Info Modal
    expect(page).to_have_title("Formation of the Metacomet Ridge | Earth Science Simulation")
    expect(page.locator("#infoModal")).not_to_have_class("hidden", timeout=1000)
    page.click("#startInvestigatingBtn")
    expect(page.locator("#infoModal")).to_have_class(re.compile(r"hidden"))

    # Verify initial simulation state via window.simulationState
    state = page.evaluate("window.simulationState")
    assert state['timeMa'] == 200
    assert state['isPlaying'] is False
    assert state['riftDepth'] == 0
    assert state['tiltAngle'] == 0
    assert state['sedimentLayers'] == 0
    assert state['basaltFlows'] == 0

def test_timeline_slider_updates_state(page: Page, sim_url: str):
    page.route('**/*', lambda route: route.continue_() if route.request.url.startswith('file://') or any(kw in route.request.url for kw in ['tailwindcss.com', 'unpkg', 'cdn', 'cloudflare', 'fonts']) else route.abort())
    page.goto(sim_url)
    page.click("#startInvestigatingBtn")

    # Move slider to 190 Ma (Sediment Deposition)
    page.evaluate("document.getElementById('timeSlider').value = 190; document.getElementById('timeSlider').dispatchEvent(new Event('input'))")

    state = page.evaluate("window.simulationState")
    assert state['timeMa'] == 190
    assert state['sedimentLayers'] > 0
    assert state['activeProcess']['name'] == 'Sediment Deposition'
    assert state['activeProcess']['type'] == 'Surface'

    # Move slider to 184 Ma (Lava Flow)
    page.evaluate("document.getElementById('timeSlider').step = '0.5'; document.getElementById('timeSlider').value = 184.5; document.getElementById('timeSlider').dispatchEvent(new Event('input'))")

    state = page.evaluate("window.simulationState")
    assert state['timeMa'] == 184.5
    assert state['basaltFlows'] == 1
    assert state['activeProcess']['name'] == 'Lava Flow (Holyoke Basalt)'
    assert state['activeProcess']['type'] == 'Internal'

    # Move slider to 160 Ma (Faulting)
    page.evaluate("document.getElementById('timeSlider').value = 160; document.getElementById('timeSlider').dispatchEvent(new Event('input'))")

    state = page.evaluate("window.simulationState")
    assert state['timeMa'] == 160
    assert state['tiltAngle'] < 0.15 # Should be decreasing tilt from max (0.15)
    assert state['tiltAngle'] > 0 # But not 0 yet
    assert state['activeProcess']['name'] == 'Eastern Border Faulting'

    # Move slider to 1 Ma (Glaciation)
    page.evaluate("document.getElementById('timeSlider').value = 1; document.getElementById('timeSlider').dispatchEvent(new Event('input'))")

    state = page.evaluate("window.simulationState")
    assert state['timeMa'] == 1
    assert state['glacierPresent'] is True
    assert state['erosionDepth'] > 0
    assert state['activeProcess']['name'] == 'Pleistocene Glaciation'

def test_play_pause_and_reset(page: Page, sim_url: str):
    page.route('**/*', lambda route: route.continue_() if route.request.url.startswith('file://') or any(kw in route.request.url for kw in ['tailwindcss.com', 'unpkg', 'cdn', 'cloudflare', 'fonts']) else route.abort())
    page.goto(sim_url)
    page.click("#startInvestigatingBtn")

    # Ensure visibility so animation runs
    page.evaluate("Object.defineProperty(document, 'hidden', { value: false, writable: false });")

    # Start Play
    page.click("#playBtn")

    # Wait for simulation to progress
    page.wait_for_function("window.simulationState.timeMa < 200")

    state = page.evaluate("window.simulationState")
    assert state['isPlaying'] is True

    # Pause
    page.click("#playBtn")
    page.wait_for_timeout(200) # Give it a moment to pause

    state = page.evaluate("window.simulationState")
    assert state['isPlaying'] is False
    paused_time = state['timeMa']

    # Wait and verify it didn't change
    page.wait_for_timeout(200)
    state = page.evaluate("window.simulationState")
    assert state['timeMa'] == paused_time

    # Reset
    page.click("#resetBtn")

    state = page.evaluate("window.simulationState")
    assert state['isPlaying'] is False
    assert state['timeMa'] == 200
