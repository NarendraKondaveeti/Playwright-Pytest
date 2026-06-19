from config.settings import Settings

from pages.form_authentication_page import (
    FormAuthenticationPage
)


def test_valid_login(page):

    page.goto(Settings.BASE_URL)

    form_auth = (
        FormAuthenticationPage(page)
    )

    form_auth.open_form_authentication()

    form_auth.login(
        "tomsmith",
        "SuperSecretPassword!"
    )

    assert (
        "You logged into a secure area!"
        in form_auth.get_flash_message()
    )

    assert (
        "Secure Area"
        in form_auth.get_secure_area_header()
    )

    assert (
        form_auth.is_logout_visible()
        is True
    )

    assert (
        "/secure"
        in page.url
    )


def test_invalid_username(page):

    page.goto(Settings.BASE_URL)

    form_auth = (
        FormAuthenticationPage(page)
    )

    form_auth.open_form_authentication()

    form_auth.login(
        "wronguser",
        "SuperSecretPassword!"
    )

    assert (
        "Your username is invalid!"
        in form_auth.get_flash_message()
    )


def test_invalid_password(page):

    page.goto(Settings.BASE_URL)

    form_auth = (
        FormAuthenticationPage(page)
    )

    form_auth.open_form_authentication()

    form_auth.login(
        "tomsmith",
        "wrongpassword"
    )

    assert (
        "Your password is invalid!"
        in form_auth.get_flash_message()
    )


def test_logout(page):

    page.goto(Settings.BASE_URL)

    form_auth = (
        FormAuthenticationPage(page)
    )

    form_auth.open_form_authentication()

    form_auth.login(
        "tomsmith",
        "SuperSecretPassword!"
    )

    form_auth.click_logout()

    assert (
        "You logged out of the secure area!"
        in form_auth.get_flash_message()
    )

    assert (
        "/secure"
        not in page.url
    )