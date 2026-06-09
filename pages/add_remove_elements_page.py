from pages.base_page import BasePage
from locators.add_remove_elements_locators import (
    AddRemoveElementsLocators
)


class AddRemoveElementsPage(BasePage):

    def click_add_remove_link(self):

        self.click(
            AddRemoveElementsLocators.ADD_REMOVE_LINK
        )

    def click_add_element_button(self):

        self.click(
            AddRemoveElementsLocators.ADD_ELEMENT_BUTTON
        )

    def click_delete_button(self):

        self.click(
            AddRemoveElementsLocators.DELETE_BUTTON
        )

    def is_delete_button_visible(self):

        return self.page.locator(
            AddRemoveElementsLocators.DELETE_BUTTON
        ).is_visible()

    def get_delete_button_count(self):

        return self.page.locator(
            AddRemoveElementsLocators.DELETE_BUTTON
        ).count()