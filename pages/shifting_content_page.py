from playwright.sync_api import expect

from locators.shifting_content_locators import (
    ShiftingContentLocators
)


class ShiftingContentPage:

    def __init__(self, page):

        self.page = page

    def open_shifting_content_page(self):

        self.page.locator(
            ShiftingContentLocators.SHIFTING_CONTENT_LINK
        ).click()

    def open_menu_element(self):

        self.page.locator(
            ShiftingContentLocators.MENU_ELEMENT_LINK
        ).click()

    def open_image(self):

        self.page.locator(
            ShiftingContentLocators.IMAGE_LINK
        ).click()

    def open_list(self):

        self.page.locator(
            ShiftingContentLocators.LIST_LINK
        ).click()

    def click_random(self):

        self.page.locator(
            ShiftingContentLocators.RANDOM_LINK
        ).click()

    def click_pixel_shift(self):

        self.page.locator(
            ShiftingContentLocators.PIXEL_SHIFT_LINK
        ).click()

    def click_random_pixel(self):

        self.page.locator(
            ShiftingContentLocators.RANDOM_PIXEL_LINK
        ).click()

    def click_home(self):

        self.page.locator(
            ShiftingContentLocators.HOME_LINK
        ).click()

    def click_about(self):

        self.page.locator(
            ShiftingContentLocators.ABOUT_LINK
        ).click()

    def click_image_random(self):

        self.page.locator(
            ShiftingContentLocators.IMAGE_RANDOM_LINK
        ).click()

    def click_image_pixel_shift(self):

        self.page.locator(
            ShiftingContentLocators.IMAGE_PIXEL_LINK
        ).click()

    def click_image_random_pixel(self):

        self.page.locator(
            ShiftingContentLocators.IMAGE_RANDOM_PIXEL_LINK
        ).click()

    def click_simple_image(self):

        self.page.locator(
            ShiftingContentLocators.SIMPLE_IMAGE_LINK
        ).click()

    def verify_image_visible(self):

        expect(
            self.page.locator(
                ShiftingContentLocators.IMAGE
            )
        ).to_be_visible()

    def verify_important_information(self):

        expect(
            self.page.locator(
                ShiftingContentLocators.IMPORTANT_TEXT
            )
        ).to_be_visible()