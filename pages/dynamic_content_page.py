from pages.base_page import BasePage

from locators.dynamic_content_locators import (
    DynamicContentLocators
)


class DynamicContentPage(BasePage):

    def open_dynamic_content(self):

        self.click(
            DynamicContentLocators.DYNAMIC_CONTENT_LINK
        )

    def click_here(self):

        self.click(
            DynamicContentLocators.CLICK_HERE_LINK
        )

    def get_third_image_src(self):

        return (
            self.page
            .locator(
                DynamicContentLocators.THIRD_IMAGE
            )
            .nth(2)
            .get_attribute("src")
        )

    def get_third_content_text(self):

        return (
            self.page
            .locator(
                DynamicContentLocators.CONTENT_TEXT
            )
            .nth(2)
            .text_content()
            .strip()
        )