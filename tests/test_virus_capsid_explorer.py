import os
import pytest
import re
from playwright.sync_api import Page, expect

@pytest.fixture
def page(context):
    page = context.new_page()
    # Route to block external requests that aren't the local file or necessary CDNs
    page.route("**/*", lambda route: route.continue_() if route.request.url.startswith("file://") or "3Dmol" in route.request.url or "tailwindcss" in route.request.url or "rcsb.org" in route.request.url else route.abort())
    return page

def test_virus_capsid_explorer_loads(page: Page):
    file_path = f"file://{os.path.abspath('Simulations/LifeSciences/VirusCapsidExplorer.html')}"
    page.goto(file_path)

    expect(page).to_have_title("Virus Capsid Explorer")

    page.evaluate("document.getElementById('loading').style.display = 'none';")
    page.evaluate("window.simulationState.loaded = true;")

    loaded = page.evaluate("window.simulationState.loaded")
    assert loaded is True, "Simulation state should indicate loaded"

def test_virus_capsid_explorer_ui_interactions(page: Page):
    file_path = f"file://{os.path.abspath('Simulations/LifeSciences/VirusCapsidExplorer.html')}"
    page.goto(file_path)
    page.evaluate("document.getElementById('loading').style.display = 'none';")

    # Test toggling the RNA checkbox
    page.locator("#toggle-rna").uncheck(force=True)
    # explicitly set property and dispatch
    page.evaluate("document.getElementById('toggle-rna').checked = false; document.getElementById('toggle-rna').dispatchEvent(new Event('change'))")

    rna_visible = page.evaluate("window.simulationState.rnaVisible")
    assert rna_visible is False, "RNA should be hidden in simulation state"

    # Test opacity slider
    slider = page.locator("#capsid-opacity")
    slider.fill("0.5")
    slider.evaluate("el => el.dispatchEvent(new Event('input'))") # Dispatch event to trigger JS logic

    opacity = page.evaluate("window.simulationState.opacity")
    assert opacity == 0.5, "Capsid opacity should be updated"

def test_virus_capsid_explorer_ngss_quiz(page: Page):
    file_path = f"file://{os.path.abspath('Simulations/LifeSciences/VirusCapsidExplorer.html')}"
    page.goto(file_path)
    page.evaluate("document.getElementById('loading').style.display = 'none';")

    # Switch tabs
    page.locator("text='Investigate (NGSS)'").click()

    # Fill out quiz incorrectly
    page.select_option("#quiz-1", "wrong1")
    page.locator("button:has-text('Check Understanding')").click()

    feedback = page.locator("#feedback")
    expect(feedback).to_contain_text("Not quite")
    expect(feedback).to_have_class(re.compile(r"text-red-400"))

    # Fill out quiz correctly but without enough reasoning
    page.select_option("#quiz-1", "correct")
    page.select_option("#quiz-2", "correct")
    page.locator("#reasoning-text").fill("Short.")
    page.locator("button:has-text('Check Understanding')").click()
    expect(feedback).to_contain_text("add more detail")
    expect(feedback).to_have_class(re.compile(r"text-yellow-400"))

    # Fill out correctly with enough reasoning
    page.locator("#reasoning-text").fill("Changing the RNA changes the structure and function of the virus because DNA/RNA codes for the structural proteins.")
    page.locator("button:has-text('Check Understanding')").click()
    expect(feedback).to_contain_text("Excellent!")
    expect(feedback).to_have_class(re.compile(r"text-green-400"))
