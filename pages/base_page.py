from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        self.page.goto(url)
        self.remove_ads()

    def remove_ads(self):
        self.page.evaluate("""
            () => {
                const ads = document.querySelectorAll('#adplus-anchor, #fixedban, footer, iframe');
                ads.forEach(ad => ad.remove());
            }
        """)