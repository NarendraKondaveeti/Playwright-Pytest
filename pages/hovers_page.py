from locators.hovers_locators import (
    HoversLocators
)


class HoversPage:

    def __init__(self, page):

        self.page = page

    def open_hovers_page(self):

        self.page.locator(
            HoversLocators.HOVERS_LINK
        ).click()

    def hover_user(self, index):

        self.page.locator(
            HoversLocators.USER_IMAGES
        ).nth(index).hover()

    def get_user_name(self, index):

        return (
            self.page.locator(
                HoversLocators.USER_NAME
            )
            .nth(index)
            .text_content()
        )