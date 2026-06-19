from pages.base_page import BasePage

from locators.file_download_locators import (
    FileDownloadLocators
)


class FileDownloadPage(BasePage):

    def open_file_download(self):

        self.click(
            FileDownloadLocators
            .FILE_DOWNLOAD_LINK
        )

    def download_sample_pdf(self):

        with self.page.expect_download() as download_info:

            self.page.locator(
                FileDownloadLocators
                .SAMPLE_PDF
            ).click()

        return download_info.value