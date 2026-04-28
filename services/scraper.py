from playwright.async_api import async_playwright

class Scraper:
    def __init__(self):
        self.playwright = None
        self.browser = None

    async def start(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=False)

    async def stop(self):
        await self.browser.close()
        await self.playwright.stop()

    async def get_title(self, url: str):
        page = await self.browser.new_page()
        await page.goto(url)
        title = await page.title()
        await page.close()
        return title
