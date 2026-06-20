import pytest

from config.settings import Settings
from pages.key_presses_page import (
    KeyPressesPage
)


def test_key_presses(page):

    page.goto(Settings.BASE_URL)

    key_press = KeyPressesPage(page)

    key_press.open_key_presses_page()

    key_press.press_key("Q")
    assert key_press.get_result_message() == "You entered: Q"

    key_press.press_key("Space")
    assert key_press.get_result_message() == "You entered: SPACE"

    key_press.press_key("Backspace")
    assert key_press.get_result_message() == "You entered: BACK_SPACE"

    key_press.press_key("Control")
    assert key_press.get_result_message() == "You entered: CONTROL"