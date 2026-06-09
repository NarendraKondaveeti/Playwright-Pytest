from pages.base_page import BasePage

from locators.challenging_dom_locators import (
    ChallengingDomLocators
)


class ChallengingDomPage(BasePage):

    def open_challenging_dom(self):

        self.click(
            ChallengingDomLocators.CHALLENGING_DOM_LINK
        )

    def get_header_text(self):

        return self.get_text(
            ChallengingDomLocators.PAGE_HEADER
        )

    def get_buttons_count(self):

        return self.page.locator(
            ChallengingDomLocators.BUTTONS
        ).count()

    def get_table_rows_count(self):

        return self.page.locator(
            ChallengingDomLocators.TABLE_ROWS
        ).count()

    def click_first_edit(self):

        self.page.locator(
            ChallengingDomLocators.EDIT_LINKS
        ).first.click()

    def click_first_delete(self):

        self.page.locator(
            ChallengingDomLocators.DELETE_LINKS
        ).first.click()

    def get_current_url(self):

        return self.page.url

    def get_first_button_text(self):

        return self.page.locator(
            '.button'
        ).nth(0).text_content()


    def click_first_button(self):

        self.page.locator(
            '.button'
        ).nth(0).click()


    def get_canvas_text(self):

        return self.page.locator(
            '#canvas'
        ).get_attribute('innerHTML')

    def get_canvas_data(self):

        return self.page.locator(
            '#canvas'
        ).screenshot()