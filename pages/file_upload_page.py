from pages.base_page import BasePage

from locators.file_upload_locators import (
    FileUploadLocators
)


class FileUploadPage(BasePage):

    def open_file_upload(self):

        self.click(
            FileUploadLocators
            .FILE_UPLOAD_LINK
        )

    def upload_file(self, file_path):

        self.page.locator(
            FileUploadLocators.FILE_INPUT
        ).set_input_files(
            file_path
        )

    def click_upload(self):

        self.click(
            FileUploadLocators
            .UPLOAD_BUTTON
        )

    def get_uploaded_file_name(self):

        return (
            self.page.locator(
                FileUploadLocators
                .UPLOADED_FILE
            )
            .text_content()
            .strip()
        )

    def get_success_header(self):

        return (
            self.page.locator(
                FileUploadLocators
                .FILE_UPLOADED_TEXT
            )
            .text_content()
            .strip()
        )