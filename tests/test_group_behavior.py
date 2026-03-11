from playwright.sync_api import sync_playwright
import os

def test_group_behavior():
    possible_paths = [
        "Simulations/LifeSciences/GroupBehavior.html",
        "../Simulations/LifeSciences/GroupBehavior.html",
        "/app/Simulations/LifeSciences/GroupBehavior.html"
    ]

    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = os.path.abspath(path)
            break

    if not file_path:
        raise FileNotFoundError("Could not find GroupBehavior.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{file_path}", wait_until="networkidle")

        # Must evaluate this so requestAnimationFrame runs
        page.evaluate("Object.defineProperty(document, 'hidden', {value: false, writable: false})")

        # 1. Run Solitary Hunt
        page.evaluate("triggerHunt()")
        page.wait_for_timeout(500) # Run for 0.5s

        # Check timer is ticking down from 20.0s
        timer_text = page.locator("#timer-display").text_content()
        assert "Time: 20.0" not in timer_text

        # Force end the hunt so we don't have to wait 20s in the test
        page.evaluate("forceEndHunt()")
        page.wait_for_timeout(100)

        # Check that data logged
        log_rows = page.locator("#data-log tr").count()
        assert log_rows == 1

        # Check averages table
        solitary_avg = page.locator("#avg-solitary").text_content()
        assert solitary_avg != "--%"

        # 2. Run Flocking Hunt
        # Select Flocking
        page.evaluate("document.querySelectorAll('.behavior-btn')[1].click()")
        page.wait_for_timeout(100)

        # Start Hunt
        page.evaluate("triggerHunt()")
        page.wait_for_timeout(500)
        page.evaluate("forceEndHunt()")
        page.wait_for_timeout(100)

        # Check log has 2 rows
        log_rows = page.locator("#data-log tr").count()
        assert log_rows == 2

        # Check averages table
        flock_avg = page.locator("#avg-flocking").text_content()
        assert flock_avg != "--%"

        # Take screenshot for verification
        os.makedirs('/home/jules/verification', exist_ok=True)
        page.screenshot(path='/home/jules/verification/group_behavior_screenshot.png', full_page=True)

        browser.close()
        print("Group Behavior simulation test passed.")

if __name__ == "__main__":
    test_group_behavior()