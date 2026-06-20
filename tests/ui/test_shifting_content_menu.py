from config.settings import Settings


def test_menu(page):

    page.goto(
        f"{Settings.BASE_URL}/shifting_content/menu"
    )

    assert "/menu" in page.url

    page.locator(
        "a[href='/shifting_content/menu?mode=random']"
    ).click()

    assert "mode=random" in page.url

    page.go_back()

    page.locator(
        "a[href='/shifting_content/menu?pixel_shift=100']"
    ).click()

    assert "pixel_shift=100" in page.url

    page.go_back()

    page.locator(
        "a[href='/shifting_content/menu?mode=random&pixel_shift=100']"
    ).click()

    assert "mode=random" in page.url
    assert "pixel_shift=100" in page.url