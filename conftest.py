from fixtures.browser_fixture import *

from fixtures.api_fixture import *
from fixtures.db_fixture import *
import pytest

@pytest.fixture
def context(browser):

    context = browser.new_context(
        geolocation={
            "latitude": 17.532984,
            "longitude": 78.389464
        },
        permissions=["geolocation"]
    )

    yield context

    context.close()


@pytest.fixture
def page(context):

    page = context.new_page()

    yield page

    page.close()