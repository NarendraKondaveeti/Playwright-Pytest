from pages.base_page import BasePage

from locators.dynamic_loading_locators import (
    DynamicLoadingLocators
)


class DynamicLoadingPage(BasePage):

    def open_dynamic_loading(self):

        self.click(
            DynamicLoadingLocators
            .DYNAMIC_LOADING_LINK
        )

    def open_example_1(self):

        self.click(
            DynamicLoadingLocators
            .EXAMPLE_1_LINK
        )

    def open_example_2(self):

        self.click(
            DynamicLoadingLocators
            .EXAMPLE_2_LINK
        )

    def click_start(self):

        self.click(
            DynamicLoadingLocators
            .START_BUTTON
        )

    def get_hello_world_text(self):

        self.page.locator(
            DynamicLoadingLocators
            .HELLO_WORLD
        ).wait_for(
            state="visible"
        )

        return (
            self.page.locator(
                DynamicLoadingLocators
                .HELLO_WORLD
            )
            .text_content()
            .strip()
        )