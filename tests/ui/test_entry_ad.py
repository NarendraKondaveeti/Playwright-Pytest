from config.settings import Settings

from pages.entry_ad_page import (
    EntryAdPage
)


def test_entry_ad(page):

    page.goto(Settings.BASE_URL)

    entry_ad = (
        EntryAdPage(page)
    )

    entry_ad.open_entry_ad()

    assert (
        entry_ad.get_modal_title()
        == "This is a modal window"
    )

    assert (
        entry_ad.is_modal_visible()
        is True
    )

    entry_ad.click_close()

    page.locator(
        "#modal"
    ).wait_for(
        state="hidden"
    )

    assert (
        entry_ad.is_modal_visible()
        is False
    )