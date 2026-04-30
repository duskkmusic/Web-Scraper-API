from fastapi import Request


def get_scraper(request: Request):
    return request.app.state.scraper