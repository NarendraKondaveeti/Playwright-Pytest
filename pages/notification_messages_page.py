from locators.notification_messages_locators import (
    NotificationMessagesLocators
)


class NotificationMessagesPage:

    def __init__(self, page):

        self.page = page

    def open_notification_messages_page(self):

        self.page.locator(
            NotificationMessagesLocators.NOTIFICATION_MESSAGES_LINK
        ).click()

    def click_here(self):

        self.page.locator(
            NotificationMessagesLocators.CLICK_HERE_LINK
        ).click()

    def get_notification_message(self):

        return (
            self.page.locator(
                NotificationMessagesLocators.FLASH_MESSAGE
            )
            .text_content()
            .replace("×", "")
            .strip()
        )