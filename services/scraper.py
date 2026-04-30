from playwright.async_api import async_playwright
from fastapi import HTTPException

class Scraper:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.initialized = False

    async def start(self):
        if self.initialized:
            return
        
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.context = await self.browser.new_context()

        self.initialized = True

    async def stop(self):
        await self.browser.close()
        await self.playwright.stop()

    async def get_title(self, url: str):
        page = await self.context.new_page()
        try:
            await page.goto(url, timeout=10000)
            return await page.title()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            await page.close()

    async def get_h1(self, url: str):
        page = await self.context.new_page()
        try:
            await page.goto(url, timeout=10000)
            return await page.locator("h1").first.inner_text()
        finally:
            await page.close()

    async def get_links(self, url: str):
        page = await self.context.new_page()
        try:
            await page.goto(url, timeout=10000)
            hrefs = await page.locator("a").evaluate_all("elements => elements.map(el => el.href)")
            return hrefs
        finally:
            await page.close()