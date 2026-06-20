from pages.base_page import BasePage

from locators.forgot_password_locators import (
    ForgotPasswordLocators
)


class ForgotPasswordPage(BasePage):

    def open_forgot_password(self):

        self.click(
            ForgotPasswordLocators
            .FORGOT_PASSWORD_LINK
        )

    def enter_email(self, email):

        self.page.locator(
            ForgotPasswordLocators.EMAIL
        ).fill(
            email
        )

    def click_retrieve_password(self):

        self.click(
            ForgotPasswordLocators
            .RETRIEVE_PASSWORD
        )

    def get_error_message(self):

        return (
            self.page.locator(
                ForgotPasswordLocators
                .ERROR_TEXT
            )
            .text_content()
            .strip()
        )