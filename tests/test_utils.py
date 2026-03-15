from pathlib import Path
from playwright.async_api import Browser, Page

async def setup_page(browser: Browser, relative_path: str) -> Page:
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

def setup_page_sync(page, block_tailwind=False):
    """
    Synchronous helper to configure a Playwright page with common settings for local testing.
    This intercepts requests to block specific resources (like tailwind CDN if requested)
    or allow common CDNs while blocking others.
    """
    if block_tailwind:
        page.route("*cdn.tailwindcss.com*", lambda route: route.abort())
    else:
        # Default behavior: allow local and specific CDNs, block everything else to prevent timeouts
        page.route('**/*', lambda route: route.continue_() if route.request.url.startswith('file://') or any(kw in route.request.url for kw in ['tailwind', 'chart.js']) else route.abort())

    return page
