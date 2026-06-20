from locators.inputs_locators import (
    InputsLocators
)


class InputsPage:

    def __init__(self, page):

        self.page = page

    def open_inputs_page(self):

        self.page.locator(
            InputsLocators.INPUTS_LINK
        ).click()

    def enter_number(
        self,
        value
    ):

        self.page.locator(
            InputsLocators.NUMBER_INPUT
        ).fill(str(value))

    def increase_value(self):

        self.page.locator(
            InputsLocators.NUMBER_INPUT
        ).press("ArrowUp")

    def decrease_value(self):

        self.page.locator(
            InputsLocators.NUMBER_INPUT
        ).press("ArrowDown")

    def get_value(self):

        return self.page.locator(
            InputsLocators.NUMBER_INPUT
        ).input_value()