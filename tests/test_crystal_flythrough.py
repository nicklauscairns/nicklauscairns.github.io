import os
import pytest
import re
import time
from playwright.sync_api import Page, expect

@pytest.fixture
def page(context):
    page = context.new_page()
    page.route("**/*", lambda route: route.continue_() if route.request.url.startswith("file://") or "3Dmol" in route.request.url or "tailwindcss" in route.request.url else route.abort())
    return page

def bypass_loading(page):
    page.evaluate("document.getElementById('loading').classList.remove('active')")
    page.evaluate("window.simulationState.loaded = true")

def test_crystal_flythrough_loads(page: Page):
    file_path = f"file://{os.path.abspath('Simulations/PhysicalSciences/CrystalFlythrough.html')}"
    page.goto(file_path)

    expect(page).to_have_title("Crystal Lattice Flythrough")

    bypass_loading(page)

    crystal = page.evaluate("window.simulationState.currentCrystal")
    assert crystal == "nacl", "Default crystal should be NaCl"

    scale = page.evaluate("window.simulationState.scale")
    assert scale == 1, "Default scale should be 1"

def test_crystal_flythrough_supercell(page: Page):
    file_path = f"file://{os.path.abspath('Simulations/PhysicalSciences/CrystalFlythrough.html')}"
    page.goto(file_path)
    bypass_loading(page)

    # Change to a 3x3x3 bulk lattice
    slider = page.locator("#supercell-slider")
    slider.fill("3")
    slider.evaluate("el => el.dispatchEvent(new Event('input'))")

    # Wait for re-render
    page.wait_for_function("window.simulationState.scale === 3", timeout=5000)

    scale = page.evaluate("window.simulationState.scale")
    assert scale == 3, "Supercell scale should be 3"

def test_crystal_flythrough_ngss_inference(page: Page):
    file_path = f"file://{os.path.abspath('Simulations/PhysicalSciences/CrystalFlythrough.html')}"
    page.goto(file_path)
    bypass_loading(page)

    # Incorrect guess
    page.select_option("#quiz-1", "wrong1")
    page.locator("button:has-text('Submit Inference')").click()

    feedback = page.locator("#feedback")
    expect(feedback).to_contain_text("Not quite")
    expect(feedback).to_have_class(re.compile(r"text-red-400"))

    # Correct guess
    page.select_option("#quiz-1", "correct")
    page.locator("button:has-text('Submit Inference')").click()

    expect(feedback).to_contain_text("Correct")
    expect(feedback).to_have_class(re.compile(r"text-green-400"))
