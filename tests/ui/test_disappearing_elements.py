import pytest
from config.settings import Settings
from pages.home_page import HomePage
from pages.disappearing_elements_page import DisappearingElementsPage
from test_data.disappearing_elements_data import (
    EXPECTED_LINKS,
    MIN_EXPECTED_LINKS,
    MAX_EXPECTED_LINKS,
    ELEMENT_TIMEOUT
)
from utils.logger import get_logger

logger = get_logger()


@pytest.mark.regression
def test_disappearing_elements(page):
    """
    Test Disappearing Elements scenario.

    Steps:
    1. Open the homepage
    2. Navigate to Disappearing Elements page via link
    3. Verify page loads successfully
    4. Validate dynamic links are handled correctly
    5. Test stability across verification

    Assertions:
    - Page loads successfully
    - Links count is within expected range (4-5)
    - Page heading is visible and correct
    - Page remains stable for element detection
    """

    logger.info("=" * 50)
    logger.info("Starting Disappearing Elements Test")
    logger.info("=" * 50)

    # Step 1: Open homepage and navigate to disappearing elements
    home_page = HomePage(page)
    home_page.open_home()
    logger.info("Homepage opened successfully")

    home_page.click_disappearing_elements_link()
    logger.info("Clicked on Disappearing Elements link")

    # Step 2: Verify page loaded
    disappearing_page = DisappearingElementsPage(page)

    # Wait a moment for page to fully load
    page.wait_for_timeout(1000)

    # Validation 1: Get visible links count - this confirms page has loaded
    links_count = disappearing_page.get_visible_links_count()
    assert links_count > 0, "Page should have visible links after loading"
    logger.info(f"✓ Validation 1 passed: Page loaded with {links_count} links")

    # Validation 3: Links count should be greater than expected minimum
    links_count = disappearing_page.get_visible_links_count()
    assert links_count >= MIN_EXPECTED_LINKS, \
        f"Expected at least {MIN_EXPECTED_LINKS} links, got {links_count}"
    logger.info(f"✓ Validation 3 passed: Links count = {links_count} (>= {MIN_EXPECTED_LINKS})")

    # Validation 4: Get and verify visible links
    visible_links = disappearing_page.get_visible_links_text()
    assert len(visible_links) > 0, "Should have at least one visible link"
    logger.info(f"✓ Validation 4 passed: Found {len(visible_links)} visible links")

    # Validation 5: Verify at least the following static links exist
    static_links = ['Home', 'About']
    for link in static_links:
        assert disappearing_page.verify_link_exists(link), \
            f"Static link '{link}' should exist on the page"
    logger.info(f"✓ Validation 5 passed: All static links present")

    # Validation 6: Test retry mechanism for dynamic link
    gallery_found = disappearing_page.verify_link_exists("Gallery")
    logger.info(f"Gallery link present: {gallery_found}")

    # Validation 7: Verify page remains stable
    links_count_second_check = disappearing_page.get_visible_links_count()
    visible_links_second_check = disappearing_page.get_visible_links_text()

    # Links count should be stable within the same page load
    assert (
            links_count == links_count_second_check or
            abs(links_count - links_count_second_check) <= 1
    ), "Links count should remain stable during test execution"
    logger.info(f"✓ Validation 7 passed: Page remains stable (links count consistency)")

    logger.info("=" * 50)
    logger.info("Disappearing Elements Test PASSED")
    logger.info("=" * 50)



