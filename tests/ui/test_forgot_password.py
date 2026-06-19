from config.settings import Settings

from pages.forgot_password_page import (
    ForgotPasswordPage
)


def test_forgot_password(page):

    page.goto(Settings.BASE_URL)

    forgot_password = (
        ForgotPasswordPage(page)
    )

    forgot_password.open_forgot_password()

    forgot_password.enter_email(
        "test@test.com"
    )

    forgot_password.click_retrieve_password()

    assert (
        forgot_password.get_error_message()
        == "Internal Server Error"
    )