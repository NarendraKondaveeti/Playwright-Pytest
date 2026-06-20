from locators.javascript_alerts_locators import (
    JavaScriptAlertsLocators
)


class JavaScriptAlertsPage:

    def __init__(self, page):

        self.page = page

    def open_javascript_alerts_page(self):

        self.page.locator(
            JavaScriptAlertsLocators.JAVASCRIPT_ALERTS_LINK
        ).click()

    def click_js_alert(self):

        self.page.locator(
            JavaScriptAlertsLocators.JS_ALERT_BUTTON
        ).click()

    def click_js_confirm(self):

        self.page.locator(
            JavaScriptAlertsLocators.JS_CONFIRM_BUTTON
        ).click()

    def click_js_prompt(self):

        self.page.locator(
            JavaScriptAlertsLocators.JS_PROMPT_BUTTON
        ).click()

    def get_result_message(self):

        return (
            self.page.locator(
                JavaScriptAlertsLocators.RESULT_MESSAGE
            ).text_content()
        )