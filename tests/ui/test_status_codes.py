from config.settings import (
    Settings
)

from pages.status_codes_page import (
    StatusCodesPage
)


def test_status_codes(page):

    page.goto(
        Settings.BASE_URL
    )

    status = (
        StatusCodesPage(page)
    )

    # Redirect Link
    status.open_redirect_page()

    # Redirection Page
    assert (
        "redirector"
        in
        page.url
    )

    # Click Here
    status.click_redirect_here()

    # Status Codes Page
    status.verify_status_codes_page()

    # External IANA Site
    status.open_iana_website()

    status.verify_iana_website()

    # Back To Status Codes
    status.return_to_status_codes_page()

    # Status Code Validations
    for code in [
        "200",
        "301",
        "404",
        "500"
    ]:

        status.click_status_code(
            code
        )

        status.verify_status_code_page(
            code
        )

        status.click_back_to_status_codes()

        status.verify_status_codes_page()