from locators.infinite_scroll_locators import (
    InfiniteScrollLocators
)


class InfiniteScrollPage:

    def __init__(self, page):

        self.page = page

    def open_infinite_scroll_page(self):

        self.page.locator(
            InfiniteScrollLocators.INFINITE_SCROLL_LINK
        ).click()

    def get_content_count(self):

        return self.page.locator(
            InfiniteScrollLocators.SCROLL_CONTENT
        ).count()

    def scroll_down(self):

        self.page.mouse.wheel(
            0,
            3000
        )