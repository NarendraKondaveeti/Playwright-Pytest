from config.settings import Settings

from pages.checkboxes_page import (
    CheckboxesPage
)


def test_checkboxes(page):

    page.goto(Settings.BASE_URL)

    checkboxes_page = (
        CheckboxesPage(page)
    )

    checkboxes_page.open_checkboxes()

    assert (
        checkboxes_page.is_checkbox_2_checked()
        is True
    )

    checkboxes_page.uncheck_checkbox_2()

    checkboxes_page.check_checkbox_1()

    assert (
        checkboxes_page.is_checkbox_1_checked()
        is True
    )

    assert (
        checkboxes_page.is_checkbox_2_checked()
        is False
    )