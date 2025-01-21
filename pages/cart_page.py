from .base_page import BasePage


class CartPage(BasePage):
    CART_ITEM_SELECTOR = "//td[text()='{product}']"
    REMOVE_BUTTON_SELECTOR = "//td[text()='{product}']/following-sibling::td/a[text()='Delete']"

    def verify_product_in_cart(self, product: str):
        """Verify that a product is in the cart."""
        self.page.get_by_role("cell", name=product).is_visible()

    def remove_product(self, product: str):
        """Remove a product from the cart."""
        self.click(self.REMOVE_BUTTON_SELECTOR.format(product=product))
