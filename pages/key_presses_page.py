from locators.key_presses_locators import (
    KeyPressesLocators
)


class KeyPressesPage:

    def __init__(self, page):

        self.page = page

    def open_key_presses_page(self):

        self.page.locator(
            KeyPressesLocators.KEY_PRESSES_LINK
        ).click()

    def press_key(self, key):

        self.page.locator(
            KeyPressesLocators.INPUT_BOX
        ).click()

        self.page.locator(
            KeyPressesLocators.INPUT_BOX
        ).press(key)

    def get_result_message(self):

        return self.page.locator(
            KeyPressesLocators.RESULT_MESSAGE
        ).text_content()