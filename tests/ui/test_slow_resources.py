from config.settings import Settings

from pages.slow_resources_page import (
    SlowResourcesPage
)


def test_slow_resources(page):

    slow_request_time = None
    slow_status_code = None

    def capture_response(response):

        nonlocal slow_request_time
        nonlocal slow_status_code

        if "slow_external" in response.url:

            slow_status_code = response.status

            slow_request_time = (
                response.request.timing["responseEnd"]
            )

    page.on(
        "response",
        capture_response
    )

    page.goto(
        Settings.BASE_URL
    )

    slow_page = (
        SlowResourcesPage(page)
    )

    slow_page.open_slow_resources_page()

    slow_page.verify_page_heading()

    slow_page.verify_page_description()

    page.wait_for_timeout(
        32000
    )

    assert (
        slow_status_code == 503
    ), (
        f"Expected 503 "
        f"but got {slow_status_code}"
    )

    print(
        f"Slow Request Time: "
        f"{slow_request_time} ms"
    )