from pages.hovers_page import (
    HoversPage
)

from config.settings import (
    Settings
)


def test_first_user_hover(page):

    page.goto(
        Settings.BASE_URL
    )

    hover_page = (
        HoversPage(page)
    )

    hover_page.open_hovers_page()

    hover_page.hover_user(0)

    actual_name = (
        hover_page.get_user_name(0)
    )

    assert actual_name == "name: user1"