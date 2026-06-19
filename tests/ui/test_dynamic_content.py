from config.settings import Settings

from pages.dynamic_content_page import (
    DynamicContentPage
)


def test_dynamic_content(page):

    page.goto(Settings.BASE_URL)

    dynamic_page = (
        DynamicContentPage(page)
    )

    dynamic_page.open_dynamic_content()

    before_image = (
        dynamic_page.get_third_image_src()
    )

    before_text = (
        dynamic_page.get_third_content_text()
    )

    dynamic_page.click_here()

    after_image = (
        dynamic_page.get_third_image_src()
    )

    after_text = (
        dynamic_page.get_third_content_text()
    )

    assert (
        before_image != after_image
        or
        before_text != after_text
    )