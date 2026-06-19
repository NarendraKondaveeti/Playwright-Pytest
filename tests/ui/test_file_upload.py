from config.settings import Settings

from pages.file_upload_page import (
    FileUploadPage
)


def test_file_upload(page):

    page.goto(Settings.BASE_URL)

    upload_page = (
        FileUploadPage(page)
    )

    upload_page.open_file_upload()

    file_path = (
        r"C:\Users\Narendra\OneDrive\AutomationTesting"
        r"\Playwright-Pytest\downloads\sample.pdf"
    )

    upload_page.upload_file(
        file_path
    )

    upload_page.click_upload()

    assert (
        upload_page.get_success_header()
        == "File Uploaded!"
    )

    assert (
        upload_page.get_uploaded_file_name()
        == "sample.pdf"
    )