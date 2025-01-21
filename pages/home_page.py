from .base_page import BasePage


class HomePage(BasePage):
    CATEGORY_SELECTOR = "text={category}"
    PRODUCT_SELECTOR = "a:has-text('{product}')"

    def navigate_to_category(self, category: str):
        """Navigate to a specific product category."""
        self.click(self.CATEGORY_SELECTOR.format(category=category))

    def select_product(self, product: str):
        """Select a specific product."""
        self.click(self.PRODUCT_SELECTOR.format(product=product))
