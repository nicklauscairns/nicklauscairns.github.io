import os
from playwright.sync_api import sync_playwright

def test_digital_transmission():
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'PhysicalSciences', 'DigitalTransmissionAdvantage.html'))
    if not os.path.exists(html_path):
        html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Simulations', 'PhysicalScience', 'DigitalTransmissionAdvantage.html'))

    file_uri = f"file://{html_path}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(file_uri, wait_until='networkidle')

        # Allow rendering
        page.wait_for_timeout(500)

        # 1. Default State Test
        noise_level = page.evaluate("window.testingTools.getNoiseLevel()")
        assert noise_level == 10, f"Expected initial noise 10, got {noise_level}"

        original_data = page.evaluate("window.testingTools.getOriginalData()")
        analog_data = page.evaluate("window.testingTools.getAnalogData()")
        digital_data = page.evaluate("window.testingTools.getDigitalData()")

        # 2. Transmit with 10% Noise
        page.get_by_text("Transmit Image").click()
        page.wait_for_timeout(200)

        analog_data_10 = page.evaluate("window.testingTools.getAnalogData()")
        digital_data_10 = page.evaluate("window.testingTools.getDigitalData()")

        # At 10% noise, Analog should degrade (differ from original), but Digital should reconstruct perfectly
        assert analog_data_10 != original_data, "Analog data should degrade with 10% noise"
        assert digital_data_10 == original_data, "Digital data should perfectly reconstruct with 10% noise"

        analog_status = page.locator("#analog-status").inner_text()
        digital_status = page.locator("#digital-status").inner_text()
        assert "Degraded" in analog_status, f"Expected analog degraded status, got {analog_status}"
        assert "Perfectly Reconstructed" in digital_status, f"Expected digital perfect status, got {digital_status}"

        # 3. Transmit with 100% Noise
        page.evaluate("document.getElementById('noise-slider').value = 100;")
        page.evaluate("document.getElementById('noise-slider').dispatchEvent(new Event('input'))")
        page.get_by_text("Transmit Image").click()
        page.wait_for_timeout(200)

        digital_data_100 = page.evaluate("window.testingTools.getDigitalData()")

        # At 100% noise, even Digital might corrupt bits, but Analog is entirely destroyed
        assert digital_data_100 != original_data, "At 100% noise, digital should eventually fail too"

        digital_status_100 = page.locator("#digital-status").inner_text()
        assert "Corrupted" in digital_status_100, f"Expected digital corrupted status at 100% noise, got {digital_status_100}"

        browser.close()

if __name__ == "__main__":
    test_digital_transmission()
    print("All tests passed for Digital Transmission Model.")