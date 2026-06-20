from playwright.sync_api import expect

from locators.tables_locators import (
    TablesLocators
)


class TablesPage:

    def __init__(self, page):

        self.page = page

    def open_tables_page(self):

        self.page.locator(
            TablesLocators.TABLES_LINK
        ).click()

    def verify_tables_displayed(self):

        expect(
            self.page.locator(
                TablesLocators.TABLE1
            )
        ).to_be_visible()

        expect(
            self.page.locator(
                TablesLocators.TABLE2
            )
        ).to_be_visible()

    def verify_table1_row_count(self):

        rows = self.page.locator(
            TablesLocators.TABLE1_ROWS
        ).count()

        assert rows == 4

    def verify_table2_row_count(self):

        rows = self.page.locator(
            TablesLocators.TABLE2_ROWS
        ).count()

        assert rows == 4

    def verify_smith_row(self):

        row = self.page.locator(
            "#table1 tbody tr"
        ).nth(0)

        assert "Smith" in row.text_content()

        assert "John" in row.text_content()

        assert "jsmith@gmail.com" in row.text_content()

    def verify_edit_delete_links(self):

        expect(
            self.page.locator(
                TablesLocators.EDIT_LINK
            )
        ).to_be_visible()

        expect(
            self.page.locator(
                TablesLocators.DELETE_LINK
            )
        ).to_be_visible()

    def verify_sorting(self):

        self.page.locator(
            TablesLocators.LAST_NAME_HEADER_TABLE1
        ).click()

        first_row = (
            self.page.locator(
                "#table1 tbody tr"
            )
            .first
            .locator("td")
            .first
            .text_content()
        )

        assert first_row == "Bach"

        self.page.locator(
            TablesLocators.LAST_NAME_HEADER_TABLE1
        ).click()

        first_row = (
            self.page.locator(
                "#table1 tbody tr"
            )
            .first
            .locator("td")
            .first
            .text_content()
        )

        assert first_row == "Smith"