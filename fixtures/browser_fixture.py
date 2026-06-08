import pytest
from playwright.sync_api import sync_playwright
from config.settings import Settings

@pytest.fixture(scope="function")
def page():

    with sync_playwright() as p:

        browser = getattr(p, Settings.BROWSER).launch(
            headless=Settings.HEADLESS,
            slow_mo=1000
        )

        page = browser.new_page()

        yield page

        browser.close()