from config.settings import Settings

from pages.dropdown_page import (
    DropdownPage
)


def test_dropdown(page):

    page.goto(Settings.BASE_URL)

    dropdown_page = (
        DropdownPage(page)
    )

    dropdown_page.open_dropdown_page()

    assert (
        dropdown_page.get_selected_option()
        == ""
    )

    dropdown_page.select_option_1()

    assert (
        dropdown_page.get_selected_option()
        == "1"
    )

    dropdown_page.select_option_2()

    assert (
        dropdown_page.get_selected_option()
        == "2"
    )