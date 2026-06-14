from pages.base_page import BasePage

from locators.context_menu_locators import (
    ContextMenuLocators
)


class ContextMenuPage(BasePage):

    def open_context_menu_page(self):

        self.click(
            ContextMenuLocators.CONTEXT_MENU_LINK
        )

    def right_click_box(self):

        self.page.locator(
            ContextMenuLocators.HOT_SPOT_BOX
        ).click(
            button="right"
        )