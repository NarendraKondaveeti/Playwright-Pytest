from config.settings import Settings

from pages.broken_images_page import (
    BrokenImagesPage
)


def test_broken_images(page):

    page.goto(Settings.BASE_URL)

    broken_images_page = (
        BrokenImagesPage(page)
    )

    broken_images_page.click_broken_images_link()

    broken_count = (
        broken_images_page.get_broken_images_count()
    )

    assert broken_count == 2