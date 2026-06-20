from playwright.sync_api import expect

from locators.status_codes_locators import (
    StatusCodesLocators
)


class StatusCodesPage:

    def __init__(self, page):

        self.page = page

    def open_redirect_page(self):

        self.page.locator(
            StatusCodesLocators.REDIRECT_LINK
        ).click()

    def click_redirect_here(self):

        self.page.locator(
            StatusCodesLocators.REDIRECT_HERE_LINK
        ).click()

    def verify_status_codes_page(self):

        expect(
            self.page.locator(
                StatusCodesLocators.STATUS_CODES_HEADING
            )
        ).to_have_text(
            "Status Codes"
        )

    def open_iana_website(self):

        self.page.locator(
            StatusCodesLocators.EXTERNAL_HERE_LINK
        ).click()

        self.page.wait_for_load_state()

    def verify_iana_website(self):

        assert (
            "iana.org"
            in
            self.page.url.lower()
        )

        assert (
            self.page.title()
            != ""
        )

    def return_to_status_codes_page(self):

        self.page.go_back()

        self.page.wait_for_load_state()

        expect(
            self.page.locator(
                StatusCodesLocators.STATUS_CODES_HEADING
            )
        ).to_have_text(
            "Status Codes"
        )

    def click_status_code(
        self,
        code
    ):

        self.page.locator(
            f"a[href='status_codes/{code}']"
        ).click()

    def verify_status_code_page(
        self,
        code
    ):

        assert (
            f"/status_codes/{code}"
            in
            self.page.url
        )

        content = (
            self.page.locator(
                StatusCodesLocators.PAGE_CONTENT
            ).text_content()
        )

        assert (
            f"This page returned a {code} status code."
            in
            content
        )

    def click_back_to_status_codes(self):

        self.page.locator(
            StatusCodesLocators.BACK_TO_STATUS_CODES_LINK
        ).click()