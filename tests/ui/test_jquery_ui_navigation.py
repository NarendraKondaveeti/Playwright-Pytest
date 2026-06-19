from pages.jquery_ui_menu_page import (
    JQueryUIMenuPage
)

from config.settings import (
    Settings
)


def test_jquery_navigation(page):

    page.goto(
        Settings.BASE_URL
    )

    jquery = (
        JQueryUIMenuPage(page)
    )

    jquery.open_jquery_ui_menu()

    jquery.hover_enabled()

    jquery.click_back_to_jquery_ui()

    assert "jqueryui" in page.url

    jquery.click_menu()

    assert "menu" in page.url