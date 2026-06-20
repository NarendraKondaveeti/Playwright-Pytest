from playwright.sync_api import expect

from config.settings import Settings


def test_image(page):

    page.goto(
        f"{Settings.BASE_URL}/shifting_content/image"
    )

    image = page.locator(
        ".example img"
    )

    expect(
        image
    ).to_be_visible()

    page.locator(
        "a[href='/shifting_content/image?mode=random']"
    ).click()

    expect(
        image
    ).to_be_visible()

    page.go_back()

    page.locator(
        "a[href='/shifting_content/image?pixel_shift=100']"
    ).click()

    expect(
        image
    ).to_be_visible()

    page.go_back()

    page.locator(
        "a[href='/shifting_content/image?mode=random&pixel_shift=100']"
    ).click()

    expect(
        image
    ).to_be_visible()

    page.go_back()

    page.locator(
        "a[href='/shifting_content/image?image_type=simple']"
    ).click()

    expect(
        image
    ).to_be_visible()