from fastapi import FastAPI
from services.scraper import Scraper

app = FastAPI()
scraper = Scraper()


@app.on_event("startup")
async def startup():
    await scraper.start()
   

@app.on_event("shutdown")
async def shutdown():
    await scraper.stop()


@app.get("/title")
async def get_title(url: str):
    title = await scrape_title(url)
    return {"title": title}

