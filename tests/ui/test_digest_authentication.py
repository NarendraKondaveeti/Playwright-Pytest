import pytest
from config.settings import Settings
from pages.home_page import HomePage
from pages.digest_auth_page import DigestAuthPage
from test_data.digest_auth_data import (
    USERNAME,
    PASSWORD,
    EXPECTED_SUCCESS_MESSAGE
)
from utils.logger import get_logger

logger = get_logger()


@pytest.mark.smoke
def test_digest_authentication(page):
    """
    Test Digest Authentication scenario.

    Steps:
    1. Open the homepage
    2. Navigate to Digest Authentication page via link
    3. Authenticate with valid credentials
    4. Validate successful authentication
    5. Verify success message is displayed

    Assertions:
    - Success message contains "Congratulations"
    - Authentication status is True
    - Success message matches expected text
    """

    logger.info("=" * 50)
    logger.info("Starting Digest Authentication Test")
    logger.info("=" * 50)

    # Step 1: Open homepage and navigate to digest auth
    home_page = HomePage(page)
    home_page.open_home()
    logger.info("Homepage opened successfully")

    home_page.click_digest_auth_link()
    logger.info("Clicked on Digest Auth link")

    # Step 2: Authenticate using credentials
    digest_page = DigestAuthPage(page)

    # Construct the digest auth URL
    digest_url = f"{Settings.BASE_URL}digest_auth"
    digest_page.navigate_with_auth(
        digest_url,
        USERNAME,
        PASSWORD
    )

    logger.info("navigated to digest auth page with credentials")

    # Step 3: Get success message
    success_message = digest_page.get_success_message()
    logger.info(f"Success message retrieved: {success_message}")

    # Validation 1: Success message contains "Congratulations"
    assert success_message is not None, "Success message should not be None"
    assert "Congratulations" in success_message, \
        f"Expected 'Congratulations' in message, got: {success_message}"
    logger.info("✓ Validation 1 passed: Success message contains 'Congratulations'")

    # Validation 2: Authentication status is True
    assert digest_page.is_authenticated() is True, \
        "Authentication should be successful"
    logger.info("✓ Validation 2 passed: Authentication is successful")

    # Validation 3: Success message matches expected text
    assert EXPECTED_SUCCESS_MESSAGE in success_message, \
        f"Expected '{EXPECTED_SUCCESS_MESSAGE}' in message, got: {success_message}"
    logger.info("✓ Validation 3 passed: Success message matches expected text")

    logger.info("=" * 50)
    logger.info("Digest Authentication Test PASSED")
    logger.info("=" * 50)

