from pages.geolocation_page import (
    GeolocationPage
)

from config.settings import Settings


def test_geolocation(page):

    page.goto(
        Settings.BASE_URL
    )

    geolocation = (
        GeolocationPage(page)
    )

    geolocation.open_geolocation_page()

    geolocation.click_where_am_i()

    assert (
        geolocation.get_latitude()
        is not None
    )

    assert (
        geolocation.get_longitude()
        is not None
    )