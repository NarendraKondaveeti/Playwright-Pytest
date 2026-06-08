from pages.login_page import LoginPage
from config.settings import Settings
from test_data.basic_auth_data import (
    USERNAME,
    PASSWORD
)


def test_basic_auth(page):

    auth_url = (
        f"https://{USERNAME}:{PASSWORD}"
        "@the-internet.herokuapp.com/basic_auth"
    )

    page.goto(auth_url)

    login_page = LoginPage(page)

    actual_text = (
        login_page.get_success_message()
    )

    assert (
        "Congratulations!"
        in actual_text
    )