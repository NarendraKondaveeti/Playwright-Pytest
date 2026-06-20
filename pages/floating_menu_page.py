from pages.base_page import BasePage

from locators.floating_menu_locators import (
    FloatingMenuLocators
)


class FloatingMenuPage(BasePage):

    def open_floating_menu(self):

        self.click(
            FloatingMenuLocators
            .FLOATING_MENU_LINK
        )

    def click_home(self):

        self.click(
            FloatingMenuLocators.HOME
        )

    def click_news(self):

        self.click(
            FloatingMenuLocators.NEWS
        )

    def click_contact(self):

        self.click(
            FloatingMenuLocators.CONTACT
        )

    def click_about(self):

        self.click(
            FloatingMenuLocators.ABOUT
        )

    def is_menu_visible(self):

        return (
            self.page.locator(
                FloatingMenuLocators.MENU
            ).is_visible()
        )

    def scroll_to_bottom(self):

        self.page.evaluate(
            """
            window.scrollTo(
                0,
                document.body.scrollHeight
            )
            """
        )