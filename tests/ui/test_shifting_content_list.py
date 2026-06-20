from playwright.sync_api import expect

from config.settings import Settings


def test_list(page):

    page.goto(
        f"{Settings.BASE_URL}/shifting_content/list"
    )

    expect(
        page.get_by_text(
            "Important Information You're Looking For"
        )
    ).to_be_visible()

    expect(
        page.get_by_text(
            "Sed deleniti blanditiis odio laudantium."
        )
    ).to_be_visible()