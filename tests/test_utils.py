from pathlib import Path

async def setup_page(browser, relative_path):
    """
    Creates a new page, intercepts the tailwindcss CDN to avoid timeouts,
    and navigates to the given local HTML file.

    Args:
        browser: The Playwright browser instance.
        relative_path: The path to the HTML file relative to the Simulations directory.
                       e.g. 'PhysicalSciences/InteractiveBoatRiverCrossingSimulation.html'
    """
    page = await browser.new_page()

    # Resolve the absolute path
    filepath = Path(__file__).parent.parent / 'Simulations' / relative_path
    url = filepath.resolve().as_uri()

    # Block the tailwind CDN specifically to avoid test timeouts
    await page.route("*cdn.tailwindcss.com*", lambda route: route.abort())

    await page.goto(url, wait_until="load")

    return page
