from playwright.sync_api import sync_playwright, expect

def automacao_alesc():
    with sync_playwright as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://alesc.sc.gov.br")
        
        expect(page).to_have_title("alesc")
        


        
automacao_alesc()