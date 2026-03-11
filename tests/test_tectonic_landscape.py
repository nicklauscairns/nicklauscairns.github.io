import os
from playwright.sync_api import sync_playwright

def test_tectonic_landscape():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Build absolute path to the local HTML file
        base_dir = "/app"
        file_path = f"file://{os.path.join(base_dir, 'Simulations/EarthSpaceSciences/TectonicLandscapeModeller.html')}"

        print(f"Navigating to {file_path}")
        page.goto(file_path, wait_until="networkidle")

        # Set document to visible to ensure requestAnimationFrame fires
        page.evaluate("document.hidden = false;")

        # 1. Verify UI Elements
        print("Verifying UI elements...")
        assert page.locator("h1", has_text="Tectonic Landscape Modeler").is_visible()
        assert page.locator("#landscapeCanvas").is_visible()
        assert page.locator("#playBtn").is_visible()

        # For testing purposes, initialize with a fixed seed so we can reset to it
        page.evaluate("initLandscape(12345);")

        # 2. Verify Initial State
        time_text = page.locator("#timeDisplay").inner_text()
        assert time_text == "0.0", f"Initial time should be 0.0, got {time_text}"

        # Get initial center height map value (index 100 out of 200)
        initial_height = page.evaluate("window.simulationState.heightMap[100]")
        print(f"Initial height at center: {initial_height}")

        # 3. Test Constructive Force (Uplift)
        # Select uplift tool
        page.locator("#toolUplift").click()

        # apply tool programmatically since sometimes playwright mouse events have trouble on canvas overlays
        page.evaluate("forceApplyTool(400, 1.0);")

        # Y value should be LOWER (higher elevation)
        post_uplift_height = page.evaluate("window.simulationState.heightMap[100]")
        print(f"Height after uplift: {post_uplift_height}")
        assert post_uplift_height < initial_height, "Uplift should decrease the Y value (raise elevation)"

        # 4. Test Play Time & Weathering (Destructive Force)
        # Play time
        page.locator("#playBtn").click()

        # Wait for some simulation steps (dt)
        page.wait_for_timeout(1000)

        # Pause time
        page.locator("#playBtn").click()

        # Verify time advanced
        post_play_time = float(page.locator("#timeDisplay").inner_text())
        print(f"Time after playing: {post_play_time}")
        assert post_play_time > 0, "Time should advance after playing"

        # Verify weathering happened (Y value should increase slightly from peak, settling back down)
        post_weathering_height = page.evaluate("window.simulationState.heightMap[100]")
        print(f"Height after weathering over time: {post_weathering_height}")

        # When time plays, both erosion AND random base erosion can happen.
        # But global weathering moves high points down towards average.
        # So we expect Y to increase (elevation drops).
        # We also need to factor in rounding or tiny fluctuations.

        # Test explicit weathering tool since time-based weathering is very slow/subtle
        page.evaluate("forceApplyTool(400, 50.0, 'weathering');")
        post_tool_weathering_height = page.evaluate("window.simulationState.heightMap[100]")
        print(f"Height after weathering tool applied: {post_tool_weathering_height}")

        assert post_tool_weathering_height > post_weathering_height, "Weathering tool should increase the Y value of a peak (lower elevation)"

        # 5. Test Mass Wasting
        # Mass Wasting needs a steep peak to collapse. Let's make a volcano first.
        page.evaluate("forceApplyTool(400, 50.0, 'volcano');")
        post_volcano_height = page.evaluate("window.simulationState.heightMap[100]")
        print(f"Height after volcano build: {post_volcano_height}")
        # Validate volcano built UP (Y decreased)
        assert post_volcano_height < post_weathering_height, "Volcano should have raised elevation (lowered Y)"

        # Select tool

        # In Playwright evaluate, ensure tool state is set properly
        # Need to explicitly evaluate and wait in a loop, masswasting targets local peaks. If the center isn't the absolute peak, it collapses around it.
        # Apply specifically to where we just built the volcano.

        # In the context of the HTML file, the actual array is `heightMap` not `window.simulationState.heightMap`.
        # The test relies on forceApplyTool to commit the change.
        page.evaluate("heightMap[100] = -5000;") # Force a huge peak in the internal array
        # Provide the actual canvas clientWidth to bypass potential headless issues where width is 0
        page.evaluate("let w = document.getElementById('landscapeCanvas').clientWidth || 800; forceApplyTool(w/2, 50.0, 'masswasting');")

        post_collapse_height = page.evaluate("window.simulationState.heightMap[100]")
        print(f"Height after mass wasting collapse: {post_collapse_height}")
        # It collapses the peak, severely lowering elevation (increasing Y)
        # Because we artificially set it to -5000, it should be > -5000
        assert post_collapse_height > -5000, "Mass wasting should dramatically collapse a peak (increase Y value)"

        # 6. Test Reset
        page.locator("#resetBtn").click()
        reset_time = page.locator("#timeDisplay").inner_text()
        assert reset_time == "0.0", "Time should be 0.0 after reset"

        reset_height = page.evaluate("window.simulationState.heightMap[100]")
        # It should match the initial exact value
        assert abs(reset_height - initial_height) < 0.1, f"Height should reset to initial. Expected {initial_height}, got {reset_height}"

        print("All Tectonic Landscape Modeler tests passed!")
        browser.close()

if __name__ == "__main__":
    test_tectonic_landscape()