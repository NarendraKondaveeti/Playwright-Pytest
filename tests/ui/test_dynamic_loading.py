from config.settings import Settings

from pages.dynamic_loading_page import (
    DynamicLoadingPage
)


def test_dynamic_loading_example_1(page):

    page.goto(Settings.BASE_URL)

    dynamic_page = (
        DynamicLoadingPage(page)
    )

    dynamic_page.open_dynamic_loading()

    dynamic_page.open_example_1()

    dynamic_page.click_start()

    assert (
        dynamic_page.get_hello_world_text()
        == "Hello World!"
    )


def test_dynamic_loading_example_2(page):

    page.goto(Settings.BASE_URL)

    dynamic_page = (
        DynamicLoadingPage(page)
    )

    dynamic_page.open_dynamic_loading()

    dynamic_page.open_example_2()

    dynamic_page.click_start()

    assert (
        dynamic_page.get_hello_world_text()
        == "Hello World!"
    )