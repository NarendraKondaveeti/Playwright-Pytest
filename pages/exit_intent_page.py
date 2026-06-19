from pages.base_page import BasePage

from locators.exit_intent_locators import (
    ExitIntentLocators
)


class ExitIntentPage(BasePage):

    def open_exit_intent(self):

        self.click(
            ExitIntentLocators.EXIT_INTENT_LINK
        )

    def trigger_exit_intent(self):

        self.page.mouse.move(
            100,
            100
        )

        self.page.mouse.move(
            100,
            -10
        )

    def get_modal_title(self):

        self.page.locator(
            ExitIntentLocators.MODAL
        ).wait_for(
            state="visible"
        )

        return (
            self.page.locator(
                ExitIntentLocators.MODAL_TITLE
            )
            .text_content()
            .strip()
        )

    def click_close(self):

        self.click(
            ExitIntentLocators.CLOSE_BUTTON
        )

    def is_modal_visible(self):

        return (
            self.page.locator(
                ExitIntentLocators.MODAL
            ).is_visible()
        )