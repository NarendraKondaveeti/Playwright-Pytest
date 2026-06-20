from playwright.sync_api import expect

from locators.typos_locators import (
    TyposLocators
)


class TyposPage:

    def __init__(self, page):

        self.page = page

    def open_typos_page(self):

        self.page.locator(
            TyposLocators.TYPOS_LINK
        ).click()

    def verify_heading(self):

        expect(
            self.page.locator(
                TyposLocators.HEADING
            )
        ).to_have_text(
            "Typos"
        )

    def verify_description(self):

        expect(
            self.page.locator(
                TyposLocators.DESCRIPTION
            )
        ).to_contain_text(
            "This example demonstrates a typo"
        )

    def verify_typo_content(self):

        actual_text = (
            self.page.locator(
                TyposLocators.TYPO_TEXT
            )
            .text_content()
            .strip()
        )

        valid_texts = [

            "Sometimes you'll see a typo, other times you won't.",

            "Sometimes you'll see a typo, other times you won,t."

        ]

        assert actual_text in valid_texts, (
            f"Unexpected text: {actual_text}"
        )

        print(
            f"Displayed Text: {actual_text}"
        )