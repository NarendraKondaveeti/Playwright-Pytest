from pathlib import Path

from config.settings import Settings

from pages.file_download_page import (
    FileDownloadPage
)


def test_file_download(page):

    page.goto(Settings.BASE_URL)

    download_page = (
        FileDownloadPage(page)
    )

    download_page.open_file_download()

    download = (
        download_page
        .download_sample_pdf()
    )

    file_name = (
        download.suggested_filename
    )

    download_path = (
        Path.cwd()
        / "downloads"
        / file_name
    )

    download.save_as(
        str(download_path)
    )

    assert (
        file_name
        == "sample.pdf"
    )

    assert (
        download_path.exists()
    )