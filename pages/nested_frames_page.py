from pages.base_page import BasePage

from locators.nested_frames_locators import (
    NestedFramesLocators
)


class NestedFramesPage(BasePage):

    def open_nested_frames(self):

        self.click(
            NestedFramesLocators.FRAMES_LINK
        )

        self.click(
            NestedFramesLocators.NESTED_FRAMES_LINK
        )

    def get_left_text(self):

        return (
            self.page
            .frame_locator(
                'frame[name="frame-top"]'
            )
            .frame_locator(
                'frame[name="frame-left"]'
            )
            .locator("body")
            .text_content()
            .strip()
        )

    def get_middle_text(self):

        return (
            self.page
            .frame_locator(
                'frame[name="frame-top"]'
            )
            .frame_locator(
                'frame[name="frame-middle"]'
            )
            .locator("#content")
            .text_content()
            .strip()
        )

    def get_right_text(self):

        return (
            self.page
            .frame_locator(
                'frame[name="frame-top"]'
            )
            .frame_locator(
                'frame[name="frame-right"]'
            )
            .locator("body")
            .text_content()
            .strip()
        )

    def get_bottom_text(self):

        return (
            self.page
            .frame_locator(
                'frame[name="frame-bottom"]'
            )
            .locator("body")
            .text_content()
            .strip()
        )