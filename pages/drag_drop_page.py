from pages.base_page import BasePage
from locators.drag_drop_locators import DragDropLocators
from utils.logger import get_logger

logger = get_logger()


class DragDropPage(BasePage):
    """Page Object for Drag and Drop page"""

    def get_column_a_text(self) -> str:
        """
        Get the text content of Column A (left box).

        Returns:
            str: Text content of Column A header
        """
        try:
            text = self.page.locator(
                f'{DragDropLocators.COLUMN_A} header'
            ).text_content()
            logger.info(f"Column A content: '{text}'")
            return text.strip() if text else ""
        except Exception as e:
            logger.warning(f"Could not get Column A text: {str(e)}")
            # Try alternative selector
            try:
                text = self.page.locator(
                    f'{DragDropLocators.COLUMN_A}'
                ).text_content()
                return text.strip() if text else ""
            except Exception as e2:
                logger.error(f"Failed to get Column A text with fallback: {str(e2)}")
                return ""

    def get_column_b_text(self) -> str:
        """
        Get the text content of Column B (right box).

        Returns:
            str: Text content of Column B header
        """
        try:
            text = self.page.locator(
                f'{DragDropLocators.COLUMN_B} header'
            ).text_content()
            logger.info(f"Column B content: '{text}'")
            return text.strip() if text else ""
        except Exception as e:
            logger.warning(f"Could not get Column B text: {str(e)}")
            # Try alternative selector
            try:
                text = self.page.locator(
                    f'{DragDropLocators.COLUMN_B}'
                ).text_content()
                return text.strip() if text else ""
            except Exception as e2:
                logger.error(f"Failed to get Column B text with fallback: {str(e2)}")
                return ""

    def drag_column_a_to_column_b(self) -> bool:
        """
        Perform drag and drop operation: drag Column A to Column B.

        Returns:
            bool: True if drag operation completed successfully
        """
        try:
            source_element = self.page.locator(DragDropLocators.COLUMN_A)
            target_element = self.page.locator(DragDropLocators.COLUMN_B)

            # Wait for elements to be visible
            source_element.wait_for(state="visible", timeout=5000)
            target_element.wait_for(state="visible", timeout=5000)

            logger.info("Both drag and drop elements are visible")

            # Perform drag and drop
            source_element.drag_to(target_element)
            logger.info("Successfully performed drag and drop operation")

            # Wait for the DOM to update after drag operation
            self.page.wait_for_timeout(1000)

            return True

        except Exception as e:
            logger.error(f"Drag and drop operation failed: {str(e)}")
            return False

    def verify_initial_state(self) -> bool:
        """
        Verify that the initial state is correct (A in left, B in right).

        Returns:
            bool: True if initial state is correct
        """
        column_a = self.get_column_a_text()
        column_b = self.get_column_b_text()

        is_correct = column_a == "A" and column_b == "B"
        logger.info(f"Initial state verification: {is_correct}")

        return is_correct

    def verify_swapped_state(self) -> bool:
        """
        Verify that the swap was successful (B in left, A in right).

        Returns:
            bool: True if swap state is correct
        """
        column_a = self.get_column_a_text()
        column_b = self.get_column_b_text()

        is_swapped = column_a == "B" and column_b == "A"
        logger.info(f"Swapped state verification: {is_swapped}")

        return is_swapped

    def get_page_header(self) -> str:
        """
        Get the page heading text.

        Returns:
            str: The page heading
        """
        text = self.get_text(DragDropLocators.PAGE_HEADER)
        logger.info(f"Page header: {text}")
        return text if text else ""

    def is_page_loaded(self) -> bool:
        """
        Verify that the page has loaded successfully.

        Returns:
            bool: True if page loaded, False otherwise
        """
        try:
            # Check if both columns are visible
            column_a_visible = self.page.locator(
                DragDropLocators.COLUMN_A
            ).is_visible()
            column_b_visible = self.page.locator(
                DragDropLocators.COLUMN_B
            ).is_visible()

            is_loaded = column_a_visible and column_b_visible
            logger.info(f"Page loaded status: {is_loaded}")

            return is_loaded

        except Exception as e:
            logger.error(f"Error checking page load status: {str(e)}")
            return False



