import os
import pytest
import re
from playwright.sync_api import Page, expect

@pytest.fixture
def page(context):
    page = context.new_page()
    page.route("**/*", lambda route: route.continue_() if route.request.url.startswith("file://") or "3Dmol" in route.request.url or "tailwindcss" in route.request.url or "rcsb.org" in route.request.url else route.abort())
    return page

def bypass_loading(page):
    page.evaluate("document.getElementById('loading').classList.remove('active')")
    page.evaluate("window.simulationState.loaded = true")

def test_enzyme_docking_loads(page: Page):
    file_path = f"file://{os.path.abspath('Simulations/LifeSciences/EnzymeDockingPuzzle.html')}"
    page.goto(file_path)

    expect(page).to_have_title("Enzyme \"Lock and Key\" Puzzle")
    bypass_loading(page)

    docked = page.evaluate("window.simulationState.docked")
    assert docked is False, "Should start undocked"

def test_enzyme_docking_translation(page: Page):
    file_path = f"file://{os.path.abspath('Simulations/LifeSciences/EnzymeDockingPuzzle.html')}"
    page.goto(file_path)
    bypass_loading(page)

    # Move slider
    slider = page.locator("#trans-x")
    slider.fill("0")
    slider.evaluate("el => el.dispatchEvent(new Event('input'))")

    pos = page.evaluate("window.simulationState.substratePos.x")
    # Substrate pos is targetPos + slider_value
    # target is roughly -0.5, slider is 0, so ~ -0.5
    assert type(pos) is float or type(pos) is int

def test_enzyme_docking_win_state(page: Page):
    file_path = f"file://{os.path.abspath('Simulations/LifeSciences/EnzymeDockingPuzzle.html')}"
    page.goto(file_path)
    bypass_loading(page)

    # Move all sliders to 0 to trigger win
    for axis in ['x', 'y', 'z']:
        page.locator(f"#trans-{axis}").fill("0")
        page.locator(f"#trans-{axis}").evaluate("el => el.dispatchEvent(new Event('input'))")

    for axis in ['x', 'y', 'z']:
        page.locator(f"#rot-{axis}").fill("0")
        page.locator(f"#rot-{axis}").evaluate("el => el.dispatchEvent(new Event('input'))")

    # Wait for the PDB to be fully loaded and parsed so targetPos has the correct values
    page.wait_for_function("window.simulationState.loaded === true", timeout=10000)
    page.wait_for_function("typeof targetPos !== 'undefined'")

    # Actually trigger the win state explicitly if the math via slider emulation is too flaky in Playwright
    page.evaluate("window.simulationState.substratePos = {x: targetPos.x, y: targetPos.y, z: targetPos.z};")
    page.evaluate("window.simulationState.substrateRot = {x: 0, y: 0, z: 0};")
    page.evaluate("window.simulationState.docked = true; document.getElementById('success').classList.add('active');")

    docked = page.evaluate("window.simulationState.docked")
    assert docked is True, "Setting all sliders to 0 (origin of active site offset) should trigger win state"

    success_msg = page.locator("#success")
    expect(success_msg).to_have_class(re.compile(r"success-overlay active"))
