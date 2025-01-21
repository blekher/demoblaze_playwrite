import os
from playwright.sync_api import Page

class BasePage:
    BASE_URL = os.getenv("BASE_URL", "https://www.demoblaze.com/")

    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str = ""):
        """Navigate to the base URL with an optional path."""
        self.page.goto(f"{self.BASE_URL}{path}")

    def click(self, selector: str):
        """Click on an element by selector."""
        self.page.locator(selector).click()

    def type_text(self, selector: str, text: str):
        """Type text into an input field."""
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str) -> str:
        """Retrieve the text content of an element."""
        return self.page.locator(selector).text_content()

    def wait_for_element(self, selector: str):
        """Wait for an element to be visible."""
        self.page.wait_for_selector(selector)