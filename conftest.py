from fixtures.browser_fixture import *
from fixtures.api_fixture import *
from fixtures.db_fixture import *

import os
import pytest
import allure


# ======================================
# Hook for Test Result
# ======================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
        item,
        call
):

    outcome = yield

    report = outcome.get_result()

    setattr(
        item,
        "rep_" + report.when,
        report
    )


# ======================================
# Context Fixture
# ======================================

@pytest.fixture
def context(
        browser,
        request
):

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

    context.tracing.start(

        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield context

    page = (
        request.node.funcargs.get(
            "page"
        )
    )

    # ==============================
    # Failed Test Only
    # ==============================

    if (
            hasattr(
                request.node,
                "rep_call"
            )
            and
            request.node.rep_call.failed
    ):

        test_name = (
            request.node.name
        )

        # --------------------------
        # Screenshot
        # --------------------------

        os.makedirs(
            "reports/screenshots",
            exist_ok=True
        )

        screenshot_path = (
            f"reports/screenshots/"
            f"{test_name}.png"
        )

        page.screenshot(

            path=screenshot_path,

            full_page=True
        )

        allure.attach.file(

            screenshot_path,

            name=
            "Failure Screenshot",

            attachment_type=
            allure.attachment_type.PNG
        )

        # --------------------------
        # Trace
        # --------------------------

        os.makedirs(
            "reports/traces",
            exist_ok=True
        )

        trace_path = (
            f"reports/traces/"
            f"{test_name}.zip"
        )

        context.tracing.stop(
            path=trace_path
        )

        allure.attach.file(

            trace_path,

            name=
            "Trace File",

            attachment_type=
            allure.attachment_type.ZIP
        )

    else:

        context.tracing.stop()

    context.close()


# ======================================
# Page Fixture
# ======================================

@pytest.fixture
def page(context):

    page = context.new_page()

    yield page

    page.close()