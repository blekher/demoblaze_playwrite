from .base_page import BasePage

class ContactPage(BasePage):
    """
    Page Object for the Contact Modal.
    """
    CONTACT_LINK = "text=Contact"
    CONTACT_MODAL = "#exampleModal"
    EMAIL_INPUT = "#recipient-email"
    NAME_INPUT = "#recipient-name"
    MESSAGE_INPUT = "#message-text"
    SEND_BUTTON = "button:has-text('Send message')"

    def open_contact_form(self):
        """Open the Contact form modal."""
        self.page.get_by_role("link", name="Contact").click()
        self.wait_for_element(self.CONTACT_MODAL)

    def submit_contact_form(self, email: str, name: str, message: str):
        """Fill and submit the contact form."""
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.NAME_INPUT, name)
        self.type_text(self.MESSAGE_INPUT, message)
        self.click(self.SEND_BUTTON)
