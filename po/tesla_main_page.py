from playwright.sync_api import Page


class TeslaMainPage:
    def __init__(self, page: Page):
        self.page = page
        self.section_title = self.page.locator('section.layout__region h1')
        self.order_now_button = self.page.locator('section.tcl-badges--with-animation a[data-gtm-interaction]')

    def navigate(self):
        self.page.goto("https://www.tesla.com/")

    def open_category(self, category):
        self.page.locator(f'a[title="{category}"]').click()

    def close_location_country_dialog(self):
        self.page.locator('dialog .tds-modal-close').click()
