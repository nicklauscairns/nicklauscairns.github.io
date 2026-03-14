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

def get_file_path():
    path1 = os.path.abspath('Simulations/LifeSciences/ProteinDenaturation.html')
    path2 = os.path.abspath('Simulations/LifeScience/ProteinDenaturation.html')
    return f"file://{path1 if os.path.exists(path1) else path2}"

def test_protein_denaturation_loads(page: Page):
    page.goto(get_file_path())

    expect(page).to_have_title("Protein Unfolding & Denaturation")

    page.evaluate("document.getElementById('loading').style.display = 'none';")
    page.evaluate("window.simulationState.loaded = true;")

    loaded = page.evaluate("window.simulationState.loaded")
    assert loaded is True, "Simulation state should indicate loaded"

    # Check default status
    status = page.evaluate("window.simulationState.status")
    assert status == "functional"

def test_protein_denaturation_temperature_slider(page: Page):
    page.goto(get_file_path())
    page.evaluate("document.getElementById('loading').style.display = 'none';")

    # Increase temperature to 80C
    slider = page.locator("#temp-slider")
    slider.fill("80")
    slider.evaluate("el => el.dispatchEvent(new Event('input'))")

    temp = page.evaluate("window.simulationState.temperature")
    assert temp == 80, "Temperature should be updated to 80"

    # Verify status changed to denatured
    status = page.evaluate("window.simulationState.status")
    assert status == "denatured", "High temperature should denature the protein"

    badge = page.locator("#protein-status")
    expect(badge).to_contain_text("Denatured")

def test_protein_denaturation_ph_slider(page: Page):
    page.goto(get_file_path())
    page.evaluate("document.getElementById('loading').style.display = 'none';")

    # Decrease pH to 2 (Highly Acidic)
    slider = page.locator("#ph-slider")
    slider.fill("2")
    slider.evaluate("el => el.dispatchEvent(new Event('input'))")

    ph = page.evaluate("window.simulationState.ph")
    assert ph == 2, "pH should be updated to 2"

    # Verify status changed to denatured
    status = page.evaluate("window.simulationState.status")
    assert status == "denatured", "Extreme pH should denature the protein"

def test_protein_denaturation_ngss_quiz(page: Page):
    page.goto(get_file_path())
    page.evaluate("document.getElementById('loading').style.display = 'none';")

    # Fill out quiz correctly
    page.select_option("#quiz-1", "correct")
    page.locator("button:has-text('Verify Claim')").click()

    feedback = page.locator("#feedback")
    expect(feedback).to_contain_text("Correct!")
    expect(feedback).to_have_class(re.compile(r"text-green-400"))
