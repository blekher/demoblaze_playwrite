from pages.auth_page import AuthPage

def test_login_positive(page):
    auth_page = AuthPage(page)
    auth_page.open()
    auth_page.login("cake", "cake")
    assert "Welcome" in auth_page.get_welcome_message()
    print("Test Passed: User logged in successfully.")

