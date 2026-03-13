import os
import sys
from playwright.sync_api import sync_playwright

def test_human_migration_scenarios():
    html_path = 'file://' + os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'EarthSpaceSciences', 'HumanMigrationSettlementSimulator.html'))

    errors = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Listen for unhandled exceptions in the page
        page.on("pageerror", lambda err: errors.append(err))

        # Override visibility state for requestAnimationFrame
        page.add_init_script("Object.defineProperty(document, 'hidden', { value: false, writable: false });")

        page.goto(html_path)
        page.wait_for_timeout(500)

        def get_log_text():
            return page.locator("#logPanel").inner_text()

        def get_population():
            return int(page.locator("#popDisplay").inner_text())

        # Test Default
        page.get_by_role("button", name="Start Sim").click()
        page.wait_for_timeout(500)
        assert get_population() > 0, "Agents failed to spawn in default mode"

        # Test Nile Scenario
        page.get_by_role("button", name="🏞️ Nile River Valley Historical").click()
        page.wait_for_timeout(200)
        assert "Nile River Valley" in get_log_text()
        page.get_by_role("button", name="Start Sim").click()
        page.wait_for_timeout(500)
        assert get_population() > 0, "Agents failed to spawn in Nile scenario"

        # Test Drought Hazard (checks for recomputeAllResources ReferenceError issue)
        page.get_by_role("button", name="☀️ Severe Drought Global").click()
        page.wait_for_timeout(500)
        assert "Severe global drought" in get_log_text(), "Drought hazard failed to trigger properly"

        # Test Dust Bowl Scenario
        page.get_by_role("button", name="🌾 The Dust Bowl Historical").click()
        page.wait_for_timeout(200)
        assert "The Dust Bowl" in get_log_text()
        page.get_by_role("button", name="Start Sim").click()
        page.wait_for_timeout(500)

        # Test Flood Hazard
        page.get_by_role("button", name="🌊 River Flood Rivers").click()
        page.wait_for_timeout(500)
        assert "Massive river flooding" in get_log_text(), "Flood hazard failed to trigger properly"

        # Test Refugee Scenario
        page.get_by_role("button", name="🌊 Climate Refugees Modern").click()
        page.wait_for_timeout(200)
        assert "Climate Refugee" in get_log_text()
        page.get_by_role("button", name="Start Sim").click()
        page.wait_for_timeout(500)

        # Test Sea Level Rise
        page.get_by_role("button", name="📈 Sea Level Rise (+1m)").click()
        page.wait_for_timeout(500)
        assert "Sea level rose" in get_log_text(), "Sea level rise failed to trigger properly"

        browser.close()

        if errors:
            print("Tests failed due to JS errors:")
            for err in errors:
                print(err)
            sys.exit(1)
        else:
            print("Human Migration Simulation tests passed successfully!")

if __name__ == "__main__":
    test_human_migration_scenarios()
