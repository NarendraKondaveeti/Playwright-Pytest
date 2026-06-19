from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from config.settings import Settings
from utils.logger import get_logger

logger = get_logger()


class HomePage(BasePage):
    """HomePage class for navigating to different test scenarios from the main page."""

    def open_home(self):
        """Open the main page of the-internet.herokuapp.com"""
        logger.info(f"Opening homepage: {Settings.BASE_URL}")
        self.open(Settings.BASE_URL)

    def click_digest_auth_link(self):
        """Navigate to Digest Authentication page from homepage"""
        logger.info("Clicking on Digest Auth link")
        self.click(HomePageLocators.DIGEST_AUTH_LINK)

    def click_disappearing_elements_link(self):
        """Navigate to Disappearing Elements page from homepage"""
        logger.info("Clicking on Disappearing Elements link")
        self.click(HomePageLocators.DISAPPEARING_ELEMENTS_LINK)

    def click_drag_drop_link(self):
        """Navigate to Drag and Drop page from homepage"""
        logger.info("Clicking on Drag and Drop link")
        self.click(HomePageLocators.DRAG_DROP_LINK)
