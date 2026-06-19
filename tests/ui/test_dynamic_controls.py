from config.settings import Settings

from pages.dynamic_controls_page import (
    DynamicControlsPage
)


def test_dynamic_controls(page):

    page.goto(Settings.BASE_URL)

    dynamic_page = (
        DynamicControlsPage(page)
    )

    dynamic_page.open_dynamic_controls()

    # Remove

    dynamic_page.click_remove_add()

    page.wait_for_selector(
        "#message"
    )

    assert (
        dynamic_page.get_message()
        == "It's gone!"
    )

    assert (
        page.locator(
            "#checkbox"
        ).count()
        == 0
    )

    assert (
        dynamic_page
        .get_remove_add_button_text()
        == "Add"
    )

    # Add

    dynamic_page.click_remove_add()

    page.wait_for_selector(
        "#message"
    )

    assert (
        dynamic_page.get_message()
        == "It's back!"
    )

    assert (
        dynamic_page
        .is_checkbox_visible()
        is True
    )

    assert (
        dynamic_page
        .get_remove_add_button_text()
        == "Remove"
    )

    # Enable

    dynamic_page.click_enable_disable()

    page.wait_for_selector(
        "#message"
    )

    assert (
        dynamic_page.get_message()
        == "It's enabled!"
    )

    assert (
        dynamic_page
        .is_input_enabled()
        is True
    )

    assert (
        dynamic_page
        .get_enable_disable_button_text()
        == "Disable"
    )

    # Disable

    dynamic_page.click_enable_disable()

    page.wait_for_selector(
        "#message"
    )

    assert (
        dynamic_page.get_message()
        == "It's disabled!"
    )

    assert (
        dynamic_page
        .is_input_enabled()
        is False
    )

    assert (
        dynamic_page
        .get_enable_disable_button_text()
        == "Enable"
    )