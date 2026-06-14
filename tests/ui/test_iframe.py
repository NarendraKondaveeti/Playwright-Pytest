from config.settings import Settings

from pages.iframe_page import (
    IframePage
)


def test_iframe(page):

    page.goto(Settings.BASE_URL)

    iframe_page = (
        IframePage(page)
    )

    iframe_page.open_iframe()

    iframe_page.close_warning()

    assert (
        iframe_page.get_editor_text()
        == "Your content goes here."
    )