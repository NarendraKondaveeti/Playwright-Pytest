from pages.base_page import BasePage

from locators.dynamic_controls_locators import (
    DynamicControlsLocators
)


class DynamicControlsPage(BasePage):

    def open_dynamic_controls(self):

        self.click(
            DynamicControlsLocators
            .DYNAMIC_CONTROLS_LINK
        )

    def click_remove_add(self):

        self.click(
            DynamicControlsLocators
            .REMOVE_ADD_BUTTON
        )

    def click_enable_disable(self):

        self.click(
            DynamicControlsLocators
            .ENABLE_DISABLE_BUTTON
        )

    def get_message(self):

        return (
            self.page
            .locator(
                DynamicControlsLocators.MESSAGE
            )
            .text_content()
            .strip()
        )

    def is_checkbox_visible(self):

        return (
            self.page
            .locator(
                DynamicControlsLocators.CHECKBOX
            )
            .is_visible()
        )

    def is_input_enabled(self):

        return (
            self.page
            .locator(
                DynamicControlsLocators.INPUT_FIELD
            )
            .is_enabled()
        )

    def get_remove_add_button_text(self):

        return (
            self.page
            .locator(
                DynamicControlsLocators
                .REMOVE_ADD_BUTTON
            )
            .text_content()
            .strip()
        )

    def get_enable_disable_button_text(self):

        return (
            self.page
            .locator(
                DynamicControlsLocators
                .ENABLE_DISABLE_BUTTON
            )
            .text_content()
            .strip()
        )

    def get_input_value(self):
        return (
            self.page.locator(
                DynamicControlsLocators.INPUT_FIELD
            ).input_value()
        )