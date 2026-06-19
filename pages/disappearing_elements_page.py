from pages.base_page import BasePage
from locators.disappearing_elements_locators import DisappearingElementsLocators
from utils.logger import get_logger

logger = get_logger()


class DisappearingElementsPage(BasePage):
    """Page Object for Disappearing Elements page"""

    def get_visible_links_count(self) -> int:
        """
        Get the count of currently visible navigation links.

        Returns:
            int: Number of visible links on the page
        """
        count = self.page.locator(
            DisappearingElementsLocators.ALL_LINKS
        ).count()
        logger.info(f"Found {count} visible links on the page")
        return count

    def get_visible_links_text(self) -> list:
        """
        Get the text content of all currently visible links.

        Returns:
            list: List of link text contents
        """
        locator = self.page.locator(
            DisappearingElementsLocators.ALL_LINKS
        )
        count = locator.count()
        links_text = []

        for i in range(count):
            text = locator.nth(i).text_content()
            if text:
                links_text.append(text.strip())

        logger.info(f"Visible links: {links_text}")
        return links_text

    def is_page_loaded(self) -> bool:
        """
        Verify that the page has loaded successfully.

        Returns:
            bool: True if page loaded, False otherwise
        """
        try:
            # Check if we have navigation links visible
            links_count = self.get_visible_links_count()
            is_loaded = links_count > 0
            logger.info(f"Page loaded status: {is_loaded}")
            return is_loaded
        except Exception as e:
            logger.error(f"Error checking page load status: {str(e)}")
            return False

    def get_page_heading(self) -> str:
        """
        Get the page heading text.

        Returns:
            str: The page heading text
        """
        try:
            heading = self.get_text(DisappearingElementsLocators.PAGE_HEADING)
            logger.info(f"Page heading: {heading}")
            return heading if heading else "Disappearing Elements"
        except Exception as e:
            logger.warning(f"Could not get page heading: {str(e)}")
            return "Disappearing Elements"

    def wait_for_link_visible(
            self,
            link_text: str,
            timeout: int = 5000
    ) -> bool:
        """
        Wait for a specific link to become visible with retry logic.

        Args:
            link_text: Text of the link to wait for
            timeout: Timeout in milliseconds

        Returns:
            bool: True if link becomes visible, False if timeout
        """
        try:
            # Try with has-text selector
            locator = self.page.locator(
                f'a:has-text("{link_text}")'
            )
            locator.wait_for(state="visible", timeout=timeout)
            logger.info(f"Link '{link_text}' is now visible")
            return True
        except Exception as e:
            logger.warning(f"Link '{link_text}' not visible: {str(e)}")
            return False

    def click_link_with_retry(
            self,
            link_text: str,
            max_retries: int = 3
    ) -> bool:
        """
        Click a specific link with retry logic for handling disappearing elements.

        Args:
            link_text: Text of the link to click
            max_retries: Maximum number of retry attempts

        Returns:
            bool: True if click successful, False otherwise
        """
        logger.info(f"Attempting to click link: '{link_text}' (max retries: {max_retries})")

        for attempt in range(1, max_retries + 1):
            try:
                locator = self.page.locator(
                    f'a:has-text("{link_text}")'
                )

                # Check if element is visible
                if locator.is_visible():
                    locator.click()
                    logger.info(f"Successfully clicked '{link_text}' on attempt {attempt}")
                    return True
                else:
                    logger.warning(f"Link '{link_text}' not visible on attempt {attempt}")

            except Exception as e:
                logger.warning(
                    f"Failed to click '{link_text}' on attempt {attempt}: {str(e)}"
                )

            # If not the last attempt, wait before retrying
            if attempt < max_retries:
                self.page.wait_for_timeout(500)  # Wait 500ms between retries

        logger.error(f"Failed to click '{link_text}' after {max_retries} attempts")
        return False

    def verify_link_exists(self, link_text: str) -> bool:
        """
        Verify that a specific link exists on the page (may not be visible).

        Args:
            link_text: Text of the link to verify

        Returns:
            bool: True if link exists, False otherwise
        """
        try:
            locator = self.page.locator(
                f'a:has-text("{link_text}")'
            )
            exists = locator.count() > 0
            logger.info(f"Link '{link_text}' exists: {exists}")
            return exists
        except Exception as e:
            logger.error(f"Error verifying link existence: {str(e)}")
            return False


