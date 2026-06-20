from fixtures.browser_fixture import *
from fixtures.api_fixture import *
from fixtures.db_fixture import *

import os
import allure
import pytest


@pytest.fixture
def context(browser):

    context = browser.new_context(

        geolocation={
            "latitude": 17.532984,
            "longitude": 78.389464
        },

        permissions=[
            "geolocation"
        ],

        record_video_dir=
        "reports/videos"

    )

    # Start Trace

    context.tracing.start(

        screenshots=True,
        snapshots=True,
        sources=True

    )

    yield context

    context.close()


@pytest.fixture
def page(context):

    page = context.new_page()

    yield page

    page.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
        item,
        call
):

    outcome = yield

    report = outcome.get_result()

    if report.when != "call":
        return

    page = item.funcargs.get(
        "page"
    )

    if not page:
        return

    test_name = item.name

    # -------------------
    # Screenshot
    # -------------------

    screenshot_path = (
        f"reports/screenshots/"
        f"{test_name}.png"
    )

    os.makedirs(
        "reports/screenshots",
        exist_ok=True
    )

    page.screenshot(
        path=screenshot_path,
        full_page=True
    )

    allure.attach.file(

        screenshot_path,

        name="Screenshot",

        attachment_type=
        allure.attachment_type.PNG

    )

    # -------------------
    # Trace
    # -------------------

    trace_path = (
        f"reports/traces/"
        f"{test_name}.zip"
    )

    os.makedirs(
        "reports/traces",
        exist_ok=True
    )

    page.context.tracing.stop(
        path=trace_path
    )

    allure.attach.file(

        trace_path,

        name="Trace",

        attachment_type=
        allure.attachment_type.ZIP

    )

    # -------------------
    # Video
    # -------------------

    try:

        video_path = (
            page.video.path()
        )

        if os.path.exists(
                video_path
        ):

            allure.attach.file(

                video_path,

                name="Video",

                attachment_type=
                allure.attachment_type.WEBM

            )

    except Exception:

        pass