import pytest

from playwright.sync_api import (
    sync_playwright
)

@pytest.fixture(scope="session")
def browser(browser_name):

    with sync_playwright() as p:

        browser = getattr(
            p,
            browser_name
        ).launch(
            headless=False,
            slow_mo=1000
        )

        yield browser

        browser.close()


@pytest.fixture(scope="session")
def page(browser):

    context = browser.new_context()

    page = context.new_page()

    yield page

    context.close()


"""import pytest
from playwright.sync_api import sync_playwright
from config.settings import Settings

@pytest.fixture(scope="session")
def page():

    with sync_playwright() as p:

        browser = getattr(p, Settings.BROWSER).launch(
            headless=Settings.HEADLESS,
            slow_mo=1000
        )

        page = browser.new_page()

        yield page

        browser.close()

        print(Settings.BROWSER)"""