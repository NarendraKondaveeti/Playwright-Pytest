from config.settings import Settings
from pages.add_remove_elements_page import (
    AddRemoveElementsPage
)

def test_add_remove_elements(page):

    page.goto(Settings.BASE_URL)

    add_remove_page = (
        AddRemoveElementsPage(page)
    )

    add_remove_page.click_add_remove_link()

    add_remove_page.click_add_element_button()

    assert (
        add_remove_page.is_delete_button_visible()
    )

    add_remove_page.click_delete_button()

    assert (
        add_remove_page.get_delete_button_count()
        == 0
    )