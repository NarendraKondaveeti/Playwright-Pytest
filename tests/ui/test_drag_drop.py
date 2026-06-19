import pytest
from config.settings import Settings
from pages.home_page import HomePage
from pages.drag_drop_page import DragDropPage
from test_data.drag_drop_data import (
    ELEMENT_A_TEXT,
    ELEMENT_B_TEXT,
    INITIAL_LEFT_CONTENT,
    INITIAL_RIGHT_CONTENT,
    EXPECTED_LEFT_AFTER_DRAG,
    EXPECTED_RIGHT_AFTER_DRAG
)
from utils.logger import get_logger

logger = get_logger()


@pytest.mark.smoke
def test_drag_and_drop(page):
    """
    Test Drag and Drop scenario.

    Steps:
    1. Open the homepage
    2. Navigate to Drag and Drop page via link
    3. Verify page loads successfully
    4. Validate initial state (A in left box, B in right box)
    5. Perform drag and drop operation
    6. Validate final state (B in left box, A in right box)

    Assertions:
    - Page loads successfully
    - Initial state is correct before drag
    - Drag operation completes successfully
    - Final state is correct after drag
    - Elements swapped positions correctly
    """

    logger.info("=" * 50)
    logger.info("Starting Drag and Drop Test")
    logger.info("=" * 50)

    # Step 1: Open homepage and navigate to drag and drop
    home_page = HomePage(page)
    home_page.open_home()
    logger.info("Homepage opened successfully")

    home_page.click_drag_drop_link()
    logger.info("Clicked on Drag and Drop link")

    # Step 2: Initialize Drag and Drop page object
    drag_drop_page = DragDropPage(page)

    # Validation 1: Page loads successfully
    assert drag_drop_page.is_page_loaded() is True, \
        "Drag and Drop page should load successfully"
    logger.info("✓ Validation 1 passed: Page loaded successfully")

    # Validation 2: Verify initial state BEFORE drag operation
    logger.info("Verifying initial state before drag operation...")

    initial_column_a = drag_drop_page.get_column_a_text()
    initial_column_b = drag_drop_page.get_column_b_text()

    logger.info(f"Before Drag - Column A: '{initial_column_a}', Column B: '{initial_column_b}'")

    assert initial_column_a == INITIAL_LEFT_CONTENT, \
        f"Column A should initially contain '{INITIAL_LEFT_CONTENT}', got '{initial_column_a}'"
    logger.info(f"✓ Validation 2a passed: Column A initially contains '{INITIAL_LEFT_CONTENT}'")

    assert initial_column_b == INITIAL_RIGHT_CONTENT, \
        f"Column B should initially contain '{INITIAL_RIGHT_CONTENT}', got '{initial_column_b}'"
    logger.info(f"✓ Validation 2b passed: Column B initially contains '{INITIAL_RIGHT_CONTENT}'")

    assert drag_drop_page.verify_initial_state() is True, \
        "Initial state verification should pass"
    logger.info("✓ Validation 2c passed: Initial state verification successful")

    # Validation 3: Perform drag and drop operation
    logger.info("Performing drag and drop operation...")
    drag_success = drag_drop_page.drag_column_a_to_column_b()

    assert drag_success is True, "Drag and drop operation should complete successfully"
    logger.info("✓ Validation 3 passed: Drag and drop operation completed successfully")

    # Validation 4: Verify final state AFTER drag operation
    logger.info("Verifying final state after drag operation...")

    final_column_a = drag_drop_page.get_column_a_text()
    final_column_b = drag_drop_page.get_column_b_text()

    logger.info(f"After Drag - Column A: '{final_column_a}', Column B: '{final_column_b}'")

    assert final_column_a == EXPECTED_LEFT_AFTER_DRAG, \
        f"Column A should contain '{EXPECTED_LEFT_AFTER_DRAG}' after drag, got '{final_column_a}'"
    logger.info(f"✓ Validation 4a passed: Column A now contains '{EXPECTED_LEFT_AFTER_DRAG}'")

    assert final_column_b == EXPECTED_RIGHT_AFTER_DRAG, \
        f"Column B should contain '{EXPECTED_RIGHT_AFTER_DRAG}' after drag, got '{final_column_b}'"
    logger.info(f"✓ Validation 4b passed: Column B now contains '{EXPECTED_RIGHT_AFTER_DRAG}'")

    # Validation 5: Verify swap was successful
    assert drag_drop_page.verify_swapped_state() is True, \
        "Swapped state verification should pass"
    logger.info("✓ Validation 5 passed: Elements successfully swapped positions")

    # Validation 6: Comprehensive state check
    assert initial_column_a != final_column_a, \
        "Column A content should change after drag operation"
    assert initial_column_b != final_column_b, \
        "Column B content should change after drag operation"
    logger.info("✓ Validation 6 passed: Element positions have changed")

    logger.info("=" * 50)
    logger.info("Drag and Drop Test PASSED")
    logger.info("=" * 50)

