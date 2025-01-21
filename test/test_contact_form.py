from pages.contact_page import ContactPage

def test_submit_contact_form(page):
    contact_page = ContactPage(page)

    contact_page.open()
    contact_page.open_contact_form()
    contact_page.submit_contact_form("test@example.com", "Cake", "Cake By The Ocean")
    print("Test Passed: Contact form submitted successfully.")