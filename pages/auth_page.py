from .base_page import BasePage

class AuthPage(BasePage):
    LOGIN_LINK = "#login2"
    USERNAME_INPUT = "#loginusername"
    PASSWORD_INPUT = "#loginpassword"
    LOGIN_BUTTON = "button:has-text('Log in')"
    WELCOME_MESSAGE = "#nameofuser"

    def login(self, username: str, password: str):
        """Log in with username and password."""
        self.click(self.LOGIN_LINK)
        self.wait_for_element(self.USERNAME_INPUT)
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_welcome_message(self) -> str:
        """Get the welcome message after logging in."""
        self.wait_for_element(self.WELCOME_MESSAGE)
        return self.get_text(self.WELCOME_MESSAGE)