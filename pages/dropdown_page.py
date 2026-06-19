from pages.base_page import BasePage

from locators.dropdown_locators import (
    DropdownLocators
)


class DropdownPage(BasePage):

    def open_dropdown_page(self):

        self.click(
            DropdownLocators.DROPDOWN_LINK
        )

    def get_selected_option(self):

        return self.page.locator(
            DropdownLocators.DROPDOWN
        ).input_value()

    def select_option_1(self):

        self.page.locator(
            DropdownLocators.DROPDOWN
        ).select_option("1")

    def select_option_2(self):

        self.page.locator(
            DropdownLocators.DROPDOWN
        ).select_option("2")