import os
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture
def sim_page(page: Page):
    file_path = f"file://{os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'EarthSpaceSciences', 'CrateringHistory.html'))}"
    page.route("*tailwindcss.com*", lambda route: route.abort())
    page.goto(file_path)
    page.wait_for_selector('canvas')
    # Unhide document for animations if necessary, though logic is decoupled
    page.evaluate("Object.defineProperty(document, 'hidden', { value: false, writable: false });")
    return page

def test_initial_state(sim_page: Page):
    assert sim_page.evaluate("window.simState.currentTime") == 0
    assert sim_page.locator("#timeDisplay").inner_text() == "4.60"
    assert sim_page.locator("#earthCraterCount").inner_text() == "0"
    assert sim_page.locator("#moonCraterCount").inner_text() == "0"
    assert float(sim_page.locator("#earthRockAge").inner_text()) == 4.60
    assert float(sim_page.locator("#moonRockAge").inner_text()) == 4.60

def test_simulation_with_all_processes(sim_page: Page):
    # Enable all processes by default, they should be enabled
    assert sim_page.evaluate("document.getElementById('toggleErosion').checked") is True
    assert sim_page.evaluate("document.getElementById('toggleTectonics').checked") is True
    assert sim_page.evaluate("document.getElementById('toggleVolcanism').checked") is True

    # Run simulation forward 2000 MY (to 2.6 BYA)
    sim_page.evaluate("window.updateSimulation(2000)")

    # Check Moon: should have many craters, age unchanged
    moon_craters = int(sim_page.locator("#moonCraterCount").inner_text())
    assert moon_craters > 10, "Moon should have many craters"
    assert float(sim_page.locator("#moonRockAge").inner_text()) == 4.60, "Moon surface age should remain 4.60 BYA"

    # Check Earth: should have fewer craters than moon, age should decrease
    earth_craters = int(sim_page.locator("#earthCraterCount").inner_text())
    assert earth_craters < moon_craters, "Earth should have erased many craters compared to the Moon"
    earth_age = float(sim_page.locator("#earthRockAge").inner_text())
    assert earth_age < 4.60, "Earth surface age should have reset due to processes"

def test_simulation_without_earth_processes(sim_page: Page):
    # Disable Earth processes
    sim_page.evaluate("document.getElementById('toggleErosion').checked = false")
    sim_page.evaluate("document.getElementById('toggleTectonics').checked = false")
    sim_page.evaluate("document.getElementById('toggleVolcanism').checked = false")

    # Reset and run forward
    sim_page.evaluate("document.getElementById('resetBtn').click()")
    sim_page.evaluate("window.updateSimulation(2000)")

    # With no active processes, Earth should look like the Moon
    moon_craters = int(sim_page.locator("#moonCraterCount").inner_text())
    earth_craters = int(sim_page.locator("#earthCraterCount").inner_text())

    # Due to randomness they might not be perfectly identical but should be very close
    max_craters = max(earth_craters, moon_craters, 1)
    diff_ratio = abs(earth_craters - moon_craters) / max_craters
    assert diff_ratio < 0.3, f"Earth ({earth_craters}) and Moon ({moon_craters}) should have similar crater counts if processes are off"

    # Earth age should remain unchanged if processes are off
    assert float(sim_page.locator("#earthRockAge").inner_text()) == 4.60, "Earth age should remain 4.60 BYA if processes are off"
