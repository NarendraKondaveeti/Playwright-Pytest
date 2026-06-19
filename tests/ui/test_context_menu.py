from config.settings import Settings

from pages.context_menu_page import (
    ContextMenuPage
)


def test_context_menu(page):

    page.goto(Settings.BASE_URL)

    context_menu = (
        ContextMenuPage(page)
    )

    context_menu.open_context_menu_page()

    alert_message = None

    def handle_alert(dialog):

        nonlocal alert_message

        alert_message = dialog.message

        dialog.accept()

    page.on(
        "dialog",
        handle_alert
    )

    context_menu.right_click_box()

    assert (
        alert_message
        == "You selected a context menu"
    )
    page.mouse.click(
        100,
        100,
        button="left"
    )