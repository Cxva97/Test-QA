from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str, retries=2):
        for intento in range(retries):
            try:
                self.page.goto(url, wait_until="domcontentloaded", timeout=15000)
                self.remove_ads()
                return
            except Exception:
                if intento == retries - 1:
                    raise

    def remove_ads(self):
        self.page.evaluate("""
            () => {
                const ads = document.querySelectorAll('#adplus-anchor, #fixedban, footer, iframe');
                ads.forEach(ad => ad.remove());
            }
        """)