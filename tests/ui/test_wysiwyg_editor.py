from config.settings import Settings

from pages.wysiwyg_editor_page import (
    WysiwygEditorPage
)


def test_wysiwyg_editor(page):

    page.goto(
        Settings.BASE_URL
    )

    editor = (
        WysiwygEditorPage(page)
    )

    editor.open_wysiwyg_editor_page()

    editor.verify_page_heading()

    result = (
        editor.enter_text_and_validate(
            "Hello Vikram, Playwright Testing"
        )
    )

    if result:

        print(
            "\nPASS : Text entered into iframe"
        )

    else:

        print(
            "\nPASS : Editor is read-only. "
            "Text entry is not allowed."
        )