from pages.horizontal_slider_page import (
    HorizontalSliderPage
)

from config.settings import (
    Settings
)


def test_horizontal_slider(page):

    page.goto(
        Settings.BASE_URL
    )

    slider = (
        HorizontalSliderPage(page)
    )

    slider.open_horizontal_slider_page()

    slider.move_slider_right(4)

    actual_value = (
        slider.get_slider_value()
    )

    assert actual_value == "2"