from config.settings import Settings

from pages.nested_frames_page import (
    NestedFramesPage
)


def test_nested_frames(page):

    page.goto(Settings.BASE_URL)

    frame_page = (
        NestedFramesPage(page)
    )

    frame_page.open_nested_frames()

    assert (
        frame_page.get_left_text()
        == "LEFT"
    )

    assert (
        frame_page.get_middle_text()
        == "MIDDLE"
    )

    assert (
        frame_page.get_right_text()
        == "RIGHT"
    )

    assert (
        frame_page.get_bottom_text()
        == "BOTTOM"
    )