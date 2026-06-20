from config.settings import Settings

from pages.tables_page import (
    TablesPage
)


def test_sortable_data_tables(page):

    page.goto(
        Settings.BASE_URL
    )

    tables = (
        TablesPage(page)
    )

    tables.open_tables_page()

    tables.verify_tables_displayed()

    tables.verify_table1_row_count()

    tables.verify_table2_row_count()

    tables.verify_smith_row()

    tables.verify_edit_delete_links()

    tables.verify_sorting()