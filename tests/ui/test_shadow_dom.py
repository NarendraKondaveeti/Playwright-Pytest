from config.settings import (
    Settings
)

from pages.shadow_dom_page import (
    ShadowDomPage
)


def test_shadow_dom(page):

    page.goto(
        Settings.BASE_URL
    )

    shadow = (
        ShadowDomPage(page)
    )

    shadow.open_shadow_dom_page()

    shadow.verify_first_text()

    shadow.verify_second_text()