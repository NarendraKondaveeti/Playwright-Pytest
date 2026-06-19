from config.settings import Settings

from pages.exit_intent_page import (
    ExitIntentPage
)


def test_exit_intent(page):

    page.goto(Settings.BASE_URL)

    exit_page = (
        ExitIntentPage(page)
    )

    exit_page.open_exit_intent()

    exit_page.trigger_exit_intent()

    assert (
        exit_page.get_modal_title()
        == "This is a modal window"
    )

    assert (
        exit_page.is_modal_visible()
        is True
    )

    exit_page.click_close()

    page.locator(
        "#ouibounce-modal"
    ).wait_for(
        state="hidden"
    )

    assert (
        exit_page.is_modal_visible()
        is False
    )