from pages.base_page import BasePage
from locators.digest_auth_locators import DigestAuthLocators
from utils.logger import get_logger

logger = get_logger()


class DigestAuthPage(BasePage):
    """Page Object for Digest Authentication page"""

    def navigate_with_auth(self, url: str, username: str, password: str):
        """
        Navigate to the digest auth page with credentials in URL.

        For digest authentication, we use basic auth syntax in the URL.
        The server will handle the digest challenge-response.

        Args:
            url: The digest auth page URL
            username: Username for authentication
            password: Password for authentication
        """
        auth_url = f"https://{username}:{password}@{url.split('://')[-1]}"
        logger.info(f"Navigating to {url} with authentication credentials")
        self.page.goto(auth_url)

    def get_success_message(self) -> str:
        """
        Get the success message displayed after authentication.

        Returns:
            str: The text content of the success message
        """
        message = self.get_text(DigestAuthLocators.SUCCESS_MESSAGE)
        logger.info(f"Retrieved success message: {message}")
        return message

    def get_page_header(self) -> str:
        """
        Get the page header text.

        Returns:
            str: The text content of the page header
        """
        header = self.get_text(DigestAuthLocators.PAGE_HEADER)
        logger.info(f"Page header: {header}")
        return header

    def is_authenticated(self) -> bool:
        """
        Verify if authentication was successful by checking if success message is visible.

        Returns:
            bool: True if authenticated, False otherwise
        """
        try:
            message = self.get_success_message()
            is_auth = message and "Congratulations" in message
            logger.info(f"Authentication status: {is_auth}")
            return is_auth
        except Exception as e:
            logger.error(f"Authentication verification failed: {str(e)}")
            return False

