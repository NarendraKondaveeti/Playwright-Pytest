from pages.base_page import BasePage

from locators.iframe_locators import (
    IframeLocators
)


class IframePage(BasePage):

    def open_iframe(self):

        self.click(
            IframeLocators.FRAMES_LINK
        )

        self.click(
            IframeLocators.IFRAME_LINK
        )

    def close_warning(self):

        close_btn = self.page.locator(
            IframeLocators.CLOSE_WARNING
        )

        if close_btn.is_visible():
            close_btn.click()

    def get_editor_text(self):

        return (
            self.page
            .frame_locator(
                IframeLocators.IFRAME
            )
            .locator(
                IframeLocators.EDITOR
            )
            .text_content()
            .strip()
        )