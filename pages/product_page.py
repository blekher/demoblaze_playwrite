from .base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = "text=Add to cart"

    def add_to_cart(self):
        """Add the current product to the cart."""
        self.click(self.ADD_TO_CART_BUTTON)
        self.page.wait_for_event("dialog").accept()