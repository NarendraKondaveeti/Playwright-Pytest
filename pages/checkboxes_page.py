from pages.base_page import BasePage

from locators.checkboxes_locators import (
    CheckboxesLocators
)


class CheckboxesPage(BasePage):

    def open_checkboxes(self):

        self.click(
            CheckboxesLocators.CHECKBOXES_LINK
        )

    def is_checkbox_1_checked(self):

        return self.page.locator(
            CheckboxesLocators.CHECKBOX_1
        ).is_checked()

    def is_checkbox_2_checked(self):

        return self.page.locator(
            CheckboxesLocators.CHECKBOX_2
        ).is_checked()

    def check_checkbox_1(self):

        self.page.locator(
            CheckboxesLocators.CHECKBOX_1
        ).check()

    def uncheck_checkbox_2(self):

        self.page.locator(
            CheckboxesLocators.CHECKBOX_2
        ).uncheck()