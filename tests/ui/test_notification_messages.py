from config.settings import Settings

from pages.notification_messages_page import (
    NotificationMessagesPage
)


def test_notification_message(page):

    page.goto(
        Settings.BASE_URL
    )

    notification = (
        NotificationMessagesPage(page)
    )

    notification.open_notification_messages_page()

    notification.click_here()

    actual_message = (
        notification.get_notification_message()
    )

    expected_messages = [

        "Action successful",

        "Action unsuccesful, please try again",

        "Action unsuccessful"
    ]

    assert (
        actual_message
        in expected_messages
    )