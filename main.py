from fastapi import FastAPI
from services.scraper import Scraper
from routes.scraper import router as scraper_router


app = FastAPI()


@app.on_event("startup")
async def startup():
    app.state.scraper = Scraper()
    await app.state.scraper.start()
   

@app.on_event("shutdown")
async def shutdown():
    await app.state.scraper.stop()


app.include_router(scraper_router)
