from config.settings import (
    Settings
)

from pages.multiple_windows_page import (
    MultipleWindowsPage
)


def test_multiple_windows(page):

    page.goto(
        Settings.BASE_URL
    )

    multiple_windows = (
        MultipleWindowsPage(page)
    )

    multiple_windows.open_multiple_windows_page()

    multiple_windows.verify_multiple_windows_page()

    parent_page = page

    child_page = (
        multiple_windows.open_new_window()
    )

    child_page.wait_for_load_state()

    multiple_windows.verify_new_window_text(
        child_page
    )

    child_page.close()

    parent_page.bring_to_front()

    multiple_windows.verify_multiple_windows_page()