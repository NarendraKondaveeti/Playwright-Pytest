from locators.jquery_ui_menu_locators import (
    JQueryUIMenuLocators
)


class JQueryUIMenuPage:

    def __init__(self, page):

        self.page = page

    def open_jquery_ui_menu(self):

        self.page.locator(
            JQueryUIMenuLocators.JQUERY_UI_MENU_LINK
        ).click()

    def hover_enabled(self):

        self.page.locator(
            JQueryUIMenuLocators.ENABLED
        ).hover()

    def hover_downloads(self):

        self.page.locator(
            JQueryUIMenuLocators.DOWNLOADS
        ).hover()

    def download_pdf(self):

        with self.page.expect_download() as download_info:

            self.page.locator(
                JQueryUIMenuLocators.PDF
            ).click()

        download = download_info.value

        download.save_as(
            "downloads/menu.pdf"
        )

    def click_back_to_jquery_ui(self):

        self.page.locator(
            JQueryUIMenuLocators.BACK_TO_JQUERY_UI
        ).click()

    def click_menu(self):

        self.page.locator(
            JQueryUIMenuLocators.MENU_LINK
        ).click()