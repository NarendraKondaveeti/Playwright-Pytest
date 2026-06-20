from playwright.sync_api import expect

from locators.multiple_windows_locators import (
    MultipleWindowsLocators
)


class MultipleWindowsPage:

    def __init__(self, page):

        self.page = page

    def open_multiple_windows_page(self):

        self.page.locator(
            MultipleWindowsLocators.MULTIPLE_WINDOWS_LINK
        ).click()

    def verify_multiple_windows_page(self):

        expect(
            self.page.locator(
                MultipleWindowsLocators.OPENING_NEW_WINDOW_TEXT
            )
        ).to_be_visible()

    def open_new_window(self):

        with self.page.context.expect_page() as new_page_info:

            self.page.locator(
                MultipleWindowsLocators.CLICK_HERE_LINK
            ).click()

        return new_page_info.value

    def verify_new_window_text(
        self,
        child_page
    ):

        expect(
            child_page.locator(
                MultipleWindowsLocators.NEW_WINDOW_TEXT
            )
        ).to_have_text(
            "New Window"
        )