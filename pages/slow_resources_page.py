from playwright.sync_api import expect

from locators.slow_resources_locators import (
    SlowResourcesLocators
)


class SlowResourcesPage:

    def __init__(self, page):

        self.page = page

    def open_slow_resources_page(self):

        self.page.locator(
            SlowResourcesLocators.SLOW_RESOURCES_LINK
        ).click()

    def verify_page_heading(self):

        expect(
            self.page.locator(
                SlowResourcesLocators.PAGE_HEADING
            )
        ).to_have_text(
            "Slow Resources"
        )

    def verify_page_description(self):

        expect(
            self.page.locator(
                SlowResourcesLocators.PAGE_DESCRIPTION
            )
        ).to_contain_text(
            "rogue GET request"
        )