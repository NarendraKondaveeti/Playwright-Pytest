from locators.geolocation_locators import (
    GeolocationLocators
)


class GeolocationPage:

    def __init__(self, page):

        self.page = page

    def open_geolocation_page(self):

        self.page.locator(
            GeolocationLocators.GEOLOCATION_LINK
        ).click()

    def click_where_am_i(self):

        self.page.get_by_role(
            "button",
            name="Where am I?"
        ).click()

    def get_latitude(self):

        return self.page.locator(
            GeolocationLocators.LATITUDE
        ).text_content()

    def get_longitude(self):

        return self.page.locator(
            GeolocationLocators.LONGITUDE
        ).text_content()