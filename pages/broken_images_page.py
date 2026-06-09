from pages.base_page import BasePage

from locators.broken_images_locators import (
    BrokenImagesLocators
)


class BrokenImagesPage(BasePage):

    def click_broken_images_link(self):

        self.click(
            BrokenImagesLocators.BROKEN_IMAGES_LINK
        )

    def get_all_images(self):

        return self.page.locator(
            BrokenImagesLocators.ALL_IMAGES
        )

    def get_broken_images_count(self):

        images = self.get_all_images()

        broken_count = 0

        for index in range(images.count()):

            image = images.nth(index)

            is_loaded = image.evaluate(
                """
                img => img.complete &&
                img.naturalWidth > 0
                """
            )

            if not is_loaded:
                broken_count += 1

        return broken_count