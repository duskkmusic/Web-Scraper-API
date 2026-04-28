from fastapi import FastAPI
from services.scraper import scrape_title

app = FastAPI()

@app.get("/title")
async def get_title(url: str):
    title = await scrape_title(url)
    return {"title": title}

