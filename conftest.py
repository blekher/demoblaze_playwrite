import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    """Set up the Playwright browser."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """Set up a new browser page for each test."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()