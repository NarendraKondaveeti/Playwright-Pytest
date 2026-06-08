from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def click_basic_auth(self):

        self.click(LoginLocators.BASIC_AUTH_LINK)

    def get_success_message(self):

        return self.get_text(
            LoginLocators.SUCCESS_MESSAGE
        )