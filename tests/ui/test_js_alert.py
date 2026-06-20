from config.settings import Settings

from pages.javascript_alerts_page import (
    JavaScriptAlertsPage
)


def test_javascript_alerts(page):

    page.goto(Settings.BASE_URL)

    alerts = JavaScriptAlertsPage(page)

    alerts.open_javascript_alerts_page()

    # JS Alert
    page.once(
        "dialog",
        lambda dialog: dialog.accept()
    )

    alerts.click_js_alert()

    assert (
        alerts.get_result_message()
        ==
        "You successfully clicked an alert"
    )

    # JS Confirm OK
    page.once(
        "dialog",
        lambda dialog: dialog.accept()
    )

    alerts.click_js_confirm()

    assert (
        alerts.get_result_message()
        ==
        "You clicked: Ok"
    )

    # JS Confirm Cancel
    page.once(
        "dialog",
        lambda dialog: dialog.dismiss()
    )

    alerts.click_js_confirm()

    assert (
        alerts.get_result_message()
        ==
        "You clicked: Cancel"
    )

    # JS Prompt OK
    page.once(
        "dialog",
        lambda dialog:
        dialog.accept("Test")
    )

    alerts.click_js_prompt()

    assert (
        alerts.get_result_message()
        ==
        "You entered: Test"
    )

    # JS Prompt Cancel
    page.once(
        "dialog",
        lambda dialog:
        dialog.dismiss()
    )

    alerts.click_js_prompt()

    assert (
        alerts.get_result_message()
        ==
        "You entered: null"
    )