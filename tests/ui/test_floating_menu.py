from config.settings import Settings

from pages.floating_menu_page import (
    FloatingMenuPage
)


def test_floating_menu(page):

    page.goto(Settings.BASE_URL)

    floating_menu = (
        FloatingMenuPage(page)
    )

    floating_menu.open_floating_menu()

    assert (
        floating_menu.is_menu_visible()
        is True
    )

    floating_menu.click_home()

    assert (
        "#home"
        in page.url
    )

    floating_menu.click_news()

    assert (
        "#news"
        in page.url
    )

    floating_menu.click_contact()

    assert (
        "#contact"
        in page.url
    )

    floating_menu.click_about()

    assert (
        "#about"
        in page.url
    )

    floating_menu.scroll_to_bottom()

    assert (
        floating_menu.is_menu_visible()
        is True
    )