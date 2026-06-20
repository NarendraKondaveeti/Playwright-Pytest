from pages.base_page import BasePage

from locators.form_authentication_locators import (
    FormAuthenticationLocators
)


class FormAuthenticationPage(BasePage):

    def open_form_authentication(self):

        self.click(
            FormAuthenticationLocators
            .FORM_AUTHENTICATION_LINK
        )

    def enter_username(self, username):

        self.page.locator(
            FormAuthenticationLocators.USERNAME
        ).fill(username)

    def enter_password(self, password):

        self.page.locator(
            FormAuthenticationLocators.PASSWORD
        ).fill(password)

    def click_login(self):

        self.click(
            FormAuthenticationLocators
            .LOGIN_BUTTON
        )

    def login(
        self,
        username,
        password
    ):

        self.enter_username(
            username
        )

        self.enter_password(
            password
        )

        self.click_login()

    def get_flash_message(self):

        return (
            self.page.locator(
                FormAuthenticationLocators
                .FLASH_MESSAGE
            )
            .text_content()
            .strip()
        )

    def get_secure_area_header(self):

        return (
            self.page.locator(
                FormAuthenticationLocators
                .SECURE_AREA_HEADER
            )
            .text_content()
            .strip()
        )

    def click_logout(self):

        self.click(
            FormAuthenticationLocators
            .LOGOUT_BUTTON
        )

    def is_logout_visible(self):

        return (
            self.page.locator(
                FormAuthenticationLocators
                .LOGOUT_BUTTON
            ).is_visible()
        )