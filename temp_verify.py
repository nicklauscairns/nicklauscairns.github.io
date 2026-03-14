from playwright.sync_api import sync_playwright
import os

def verify():
    # Make sure verification dir exists
    os.makedirs('/home/jules/verification/', exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Block external CDNs except ChartJS/Tailwind if needed, though local routing is better.
        # But we must ensure the hidden property isn't true for requestAnimationFrame

        page.goto('file:///app/Simulations/EarthSpaceSciences/PuertoRicanKarstTopography.html')

        page.evaluate("Object.defineProperty(document, 'hidden', { value: false, writable: false });")

        # Close Modal
        page.click('#close-modal-btn')

        # Change slider
        page.fill('#slider-ph', '4.5')
        page.evaluate("document.getElementById('slider-ph').dispatchEvent(new Event('input'))")

        page.fill('#slider-rainfall', '3500')
        page.evaluate("document.getElementById('slider-rainfall').dispatchEvent(new Event('input'))")

        # Click Play
        page.click('#btn-play')

        # Wait a bit for simulation to run
        page.wait_for_timeout(3000)

        # Take Screenshot
        page.screenshot(path='/home/jules/verification/karst_running.png')

        browser.close()

if __name__ == '__main__':
    verify()
