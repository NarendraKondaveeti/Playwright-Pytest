from playwright.sync_api import expect

from locators.wysiwyg_editor_locators import (
    WysiwygEditorLocators
)


class WysiwygEditorPage:

    def __init__(self, page):

        self.page = page

    def open_wysiwyg_editor_page(self):

        self.page.locator(
            WysiwygEditorLocators.WYSIWYG_EDITOR_LINK
        ).click()

    def verify_page_heading(self):

        expect(
            self.page.locator(
                WysiwygEditorLocators.PAGE_HEADING
            )
        ).to_have_text(
            "An iFrame containing the TinyMCE WYSIWYG Editor"
        )

    def enter_text_and_validate(
        self,
        text
    ):

        editor = self.page.locator(
            WysiwygEditorLocators.EDITOR_CONTAINER
        )

        disabled = editor.get_attribute(
            "aria-disabled"
        )

        # Editor Read Only

        if disabled == "true":

            message = (
                self.page.locator(
                    WysiwygEditorLocators.READ_ONLY_MESSAGE
                )
                .text_content()
            )

            print(
                "\nEditor is READ ONLY"
            )

            print(
                f"Message: {message}"
            )

            return False

        # Editor Editable

        frame = self.page.frame_locator(
            WysiwygEditorLocators.EDITOR_IFRAME
        )

        body = frame.locator(
            "body"
        )

        body.click()

        body.fill(
            text
        )

        actual_text = (
            body.text_content()
            .strip()
        )

        print(
            "\nText entered successfully"
        )

        print(
            f"Entered Text: {actual_text}"
        )

        assert (
            actual_text == text
        )

        return True