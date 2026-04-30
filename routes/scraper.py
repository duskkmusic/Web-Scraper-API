from fastapi import APIRouter, Query, Depends
from schemas.scraper import TitleResponse
from dependencies.scraper import get_scraper


router = APIRouter()

@router.get("/title", response_model=TitleResponse)
async def get_title(url: str = Query(...), scraper = Depends(get_scraper)):
    title = await scraper.get_title(url)
    return {"title": title}

@router.get("/h1")
async def get_h1(url: str = Query(...), scraper = Depends(get_scraper)):
    return {"h1": await scraper.get_h1(url)}

@router.get("/links")
async def get_links(url: str = Query(...), scraper = Depends(get_scraper)):
    return {"links": await scraper.get_links(url)}