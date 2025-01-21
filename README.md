# Demoblaze Test Automation Framework

This is a Python-based test automation framework for testing the [Demoblaze online store](https://www.demoblaze.com/). The framework uses **Playwright** and **pytest** for browser automation and test execution.

---

## Features

- **Playwright Integration**: Fast and reliable browser automation.
- **Pytest Support**: Simple and scalable test runner.
- **Page Object Model (POM)**: Organized and maintainable code.
- **Reusable Fixtures**: Simplified browser and page setup.
- **HTML Test Reports**: Generate detailed test execution reports.

---

## Project Structure

```
.
├── pages/                   # Page Object Model files
│   ├── __init__.py
│   ├── base_page.py         # Base methods for all pages
│   ├── home_page.py         # Actions and locators for the home page
│   ├── product_page.py      # Actions and locators for the product details page
│   ├── cart_page.py         # Actions and locators for the cart page
│   ├── auth_page.py         # Actions and locators for login/logout
├── tests/                   # Test cases
│   ├── __init__.py
│   ├── test_add_to_cart.py  # Tests for adding products to the cart
│   ├── test_login.py        # Login tests (positive/negative)
├── conftest.py              # pytest fixtures for browser and page setup
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .env                     # Environment variables
```

---

## Prerequisites

1. Python 3.8 or higher.
2. Playwright installed.
3. Google Chrome, Microsoft Edge, or another browser supported by Playwright.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd demoblaze-framework
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

---

## Running Tests

1. Run all tests:
   ```bash
   pytest
   ```

2. Generate an HTML report:
   ```bash
   pytest --html=report.html --self-contained-html
   ```

3. Run a specific test file:
   ```bash
   pytest tests/test_add_to_cart.py
   ```

4. Run a specific test case:
   ```bash
   pytest -k "test_add_to_cart"
   ```

---

## Environment Variables

Set the `BASE_URL` for the application in a `.env` file:

```
BASE_URL=https://www.demoblaze.com/
```

---

## Key Components

### **Page Objects**
- Encapsulate locators and actions for specific pages or modals.
- Reusable across multiple tests.

### **Fixtures**
- `browser`: Sets up the Playwright browser for the session.
- `page`: Provides a fresh page instance for each test.


---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
Thanks to the Playwright and pytest communities for their tools and documentation.
