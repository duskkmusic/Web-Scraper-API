from playwright.async_api import async_playwright

async def scrape_title(url: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto(url)
        title = await page.title()

        await browser.close()
        return title
