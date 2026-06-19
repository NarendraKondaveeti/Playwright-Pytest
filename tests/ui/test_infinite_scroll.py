from pages.infinite_scroll_page import (
    InfiniteScrollPage
)

from config.settings import (
    Settings
)

import time


def test_infinite_scroll(page):

    page.goto(
        Settings.BASE_URL
    )

    infinite_scroll = (
        InfiniteScrollPage(page)
    )

    infinite_scroll.open_infinite_scroll_page()

    initial_count = (
        infinite_scroll.get_content_count()
    )

    infinite_scroll.scroll_down()

    page.wait_for_timeout(2000)

    new_count = (
        infinite_scroll.get_content_count()
    )

    assert new_count > initial_count