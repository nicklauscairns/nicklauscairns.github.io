import json
import time
from playwright.sync_api import sync_playwright

def run_sim():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('file:///app/Simulations/LifeSciences/PredatorPrey.html')

        # Wait a bit for initialization
        time.sleep(2)

        # Click start
        page.locator('#startBtn').click()

        # Run for 15 seconds and record stats to see longer trends
        stats = []
        for i in range(15):
            time.sleep(1)
            prey = page.locator('#currentPrey').text_content()
            pred = page.locator('#currentPred').text_content()
            stats.append({'time': i+1, 'prey': int(prey), 'pred': int(pred)})
            print(f"Second {i+1}: Prey {prey}, Pred {pred}")

        print("Simulation Stats:", json.dumps(stats, indent=2))
        browser.close()

if __name__ == '__main__':
    run_sim()
