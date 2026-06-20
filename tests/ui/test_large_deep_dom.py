from config.settings import Settings

from pages.large_deep_dom_page import (
    LargeDeepDomPage
)


def test_large_deep_dom(page):

    page.goto(
        Settings.BASE_URL
    )

    large_dom = (
        LargeDeepDomPage(page)
    )

    large_dom.open_large_deep_dom_page()

    large_dom.verify_large_dom_page_opened()

    large_dom.verify_no_siblings_text()

    large_dom.verify_large_table_visible()

    large_dom.scroll_to_bottom()

    large_dom.scroll_to_top()