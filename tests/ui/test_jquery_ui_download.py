from pages.jquery_ui_menu_page import (
    JQueryUIMenuPage
)

from config.settings import (
    Settings
)


def test_pdf_download(page):

    page.goto(
        Settings.BASE_URL
    )

    jquery = (
        JQueryUIMenuPage(page)
    )

    jquery.open_jquery_ui_menu()

    jquery.hover_enabled()

    jquery.hover_downloads()

    jquery.download_pdf()