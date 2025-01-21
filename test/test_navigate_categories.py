from pages.home_page import HomePage

def test_navigate_categories(page):
    home_page = HomePage(page)

    home_page.open()
    home_page.navigate_to_category("Phones")
    assert "Phones" in page.content(), "Failed to navigate to Phones category!"

    home_page.navigate_to_category("Laptops")
    assert "Laptops" in page.content(), "Failed to navigate to Laptops category!"

    home_page.navigate_to_category("Monitors")
    assert "Monitors" in page.content(), "Failed to navigate to Monitors category!"
    print("Test Passed: Category navigation verified successfully.")