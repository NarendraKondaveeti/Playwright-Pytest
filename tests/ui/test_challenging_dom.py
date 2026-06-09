from config.settings import Settings

from pages.challenging_dom_page import (
    ChallengingDomPage
)


def test_challenging_dom(page):

    page.goto(Settings.BASE_URL)

    dom_page = ChallengingDomPage(page)

    dom_page.open_challenging_dom()

    assert (
        dom_page.get_header_text()
        == "Challenging DOM"
    )

    assert (
        dom_page.get_buttons_count()
        == 3
    )

    assert (
        dom_page.get_table_rows_count()
        == 10
    )

    before_text = (
        dom_page.get_first_button_text()
    )

    dom_page.click_first_button()

    after_text = (
        dom_page.get_first_button_text()
    )

    assert (
        before_text != after_text
    )

    dom_page.click_first_edit()

    assert (
        "#edit"
        in dom_page.get_current_url()
    )

    dom_page.click_first_delete()

    assert (
        "#delete"
        in dom_page.get_current_url()
    )