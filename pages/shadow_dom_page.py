from playwright.sync_api import expect

from locators.shadow_dom_locators import (
    ShadowDomLocators
)


class ShadowDomPage:

    def __init__(self, page):

        self.page = page

    def open_shadow_dom_page(self):

        self.page.locator(
            ShadowDomLocators.SHADOW_DOM_LINK
        ).click()

    def verify_first_text(self):

        expect(
            self.page.locator(
                ShadowDomLocators.FIRST_TEXT
            ).first
        ).to_have_text(
            "Let's have some different text!"
        )

    def verify_second_text(self):

        expect(
            self.page.locator(
                ShadowDomLocators.SECOND_TEXT
            )
        ).to_have_text(
            "In a list!"
        )