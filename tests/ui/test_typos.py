from config.settings import Settings

from pages.typos_page import (
    TyposPage
)


def test_typos(page):

    page.goto(
        Settings.BASE_URL
    )

    typos = (
        TyposPage(page)
    )

    typos.open_typos_page()

    typos.verify_heading()

    typos.verify_description()

    typos.verify_typo_content()