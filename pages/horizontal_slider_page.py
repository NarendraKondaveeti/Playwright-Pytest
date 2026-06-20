from playwright.sync_api import (
    expect
)

from locators.horizontal_slider_locators import (
    HorizontalSliderLocators
)


class HorizontalSliderPage:

    def __init__(self, page):

        self.page = page

    def open_horizontal_slider_page(self):

        self.page.locator(
            HorizontalSliderLocators.HORIZONTAL_SLIDER_LINK
        ).click()

    def move_slider_right(self, count):

        slider = self.page.locator(
            HorizontalSliderLocators.SLIDER
        )

        slider.focus()

        for _ in range(count):

            slider.press("ArrowRight")

    def move_slider_left(self, count):

        slider = self.page.locator(
            HorizontalSliderLocators.SLIDER
        )

        slider.focus()

        for _ in range(count):

            slider.press("ArrowLeft")

    def get_slider_value(self):

        return self.page.locator(
            HorizontalSliderLocators.RANGE_VALUE
        ).text_content()