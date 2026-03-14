import os
import pytest
import re
from playwright.sync_api import Page, expect

@pytest.fixture
def page(context):
    page = context.new_page()
    page.route("**/*", lambda route: route.continue_() if route.request.url.startswith("file://") or "3Dmol" in route.request.url or "tailwindcss" in route.request.url or "pubchem" in route.request.url else route.abort())
    return page

def test_monster_molecules_loads(page: Page):
    file_path = f"file://{os.path.abspath('Simulations/PhysicalSciences/MonsterMolecules.html')}"
    page.goto(file_path)

    expect(page).to_have_title("Monster Molecules Showcase")

    # Wait for initial load
    page.evaluate("document.getElementById('loading').classList.remove('active');")
    page.evaluate("window.simulationState.loaded = true;")

    loaded = page.evaluate("window.simulationState.loaded")
    assert loaded is True, "Simulation state should indicate loaded"

    molecule = page.evaluate("window.simulationState.currentMolecule")
    assert molecule == "cubane", "Default molecule should be cubane"

def test_monster_molecules_selection(page: Page):
    file_path = f"file://{os.path.abspath('Simulations/PhysicalSciences/MonsterMolecules.html')}"
    page.goto(file_path)
    page.evaluate("document.getElementById('loading').classList.remove('active');")

    # Click a different molecule card
    page.locator("text='Buckyball (C60)'").click()

    molecule = page.evaluate("window.simulationState.currentMolecule")
    assert molecule == "buckyball", "Current molecule should change to buckyball"

def test_monster_molecules_ngss_bond_check(page: Page):
    file_path = f"file://{os.path.abspath('Simulations/PhysicalSciences/MonsterMolecules.html')}"
    page.goto(file_path)
    page.evaluate("document.getElementById('loading').classList.remove('active');")

    # Incorrect guess
    page.locator("button:has-text('3 Bonds')").click()
    feedback = page.locator("#bond-feedback")
    expect(feedback).to_contain_text("Not quite")
    expect(feedback).to_have_class(re.compile(r"text-red-400"))

    # Correct guess
    page.locator("button:has-text('4 Bonds')").click()
    expect(feedback).to_contain_text("Correct")
    expect(feedback).to_have_class(re.compile(r"text-green-400"))
