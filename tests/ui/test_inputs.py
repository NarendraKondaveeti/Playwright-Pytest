from pages.inputs_page import (
    InputsPage
)

from config.settings import (
    Settings
)


def test_manual_input(page):

    page.goto(
        Settings.BASE_URL
    )

    inputs = (
        InputsPage(page)
    )

    inputs.open_inputs_page()

    inputs.enter_number(100)

    actual_value = (
        inputs.get_value()
    )

    assert actual_value == "100"


def test_arrow_up(page):

    page.goto(
        Settings.BASE_URL
    )

    inputs = (
        InputsPage(page)
    )

    inputs.open_inputs_page()

    inputs.enter_number(5)

    inputs.increase_value()

    actual_value = (
        inputs.get_value()
    )

    assert actual_value == "6"


def test_arrow_down(page):

    page.goto(
        Settings.BASE_URL
    )

    inputs = (
        InputsPage(page)
    )

    inputs.open_inputs_page()

    inputs.enter_number(5)

    inputs.decrease_value()

    actual_value = (
        inputs.get_value()
    )

    assert actual_value == "4"