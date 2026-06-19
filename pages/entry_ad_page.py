from pages.base_page import BasePage

from locators.entry_ad_locators import (
    EntryAdLocators
)


class EntryAdPage(BasePage):

    def open_entry_ad(self):

        self.click(
            EntryAdLocators.ENTRY_AD_LINK
        )

    def get_modal_title(self):

        self.page.locator(
            EntryAdLocators.MODAL
        ).wait_for(
            state="visible"
        )

        return (
            self.page.locator(
                EntryAdLocators.MODAL_TITLE
            )
            .text_content()
            .strip()
        )

    def click_close(self):

        self.click(
            EntryAdLocators.CLOSE_BUTTON
        )

    def is_modal_visible(self):

        return (
            self.page.locator(
                EntryAdLocators.MODAL
            ).is_visible()
        )

    def click_restart_ad(self):

        self.click(
            EntryAdLocators.RESTART_AD
        )