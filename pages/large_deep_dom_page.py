from playwright.sync_api import expect

from locators.large_deep_dom_locators import (
    LargeDeepDomLocators
)


class LargeDeepDomPage:

    def __init__(self, page):

        self.page = page

    def open_large_deep_dom_page(self):

        self.page.locator(
            LargeDeepDomLocators.LARGE_DEEP_DOM_LINK
        ).click()

    def verify_large_dom_page_opened(self):

        assert "/large" in self.page.url

    def verify_no_siblings_text(self):

        expect(
            self.page.locator(
                LargeDeepDomLocators.NO_SIBLINGS_TEXT
            )
        ).to_have_text(
            "No siblings"
        )

    def verify_large_table_visible(self):

        expect(
            self.page.locator(
                LargeDeepDomLocators.LARGE_TABLE
            )
        ).to_be_visible()

    def scroll_to_bottom(self):

        self.page.evaluate(
            "window.scrollTo(0, document.body.scrollHeight)"
        )

    def scroll_to_top(self):

        self.page.evaluate(
            "window.scrollTo(0, 0)"
        )