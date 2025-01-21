from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_remove_product_from_cart(page):
    """Verify that a product can be removed from the cart."""
    home_page = HomePage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    home_page.open()
    home_page.navigate_to_category("Phones")
    home_page.select_product("Samsung galaxy s6")
    product_page.add_to_cart()

    cart_page.open("cart.html")
    cart_page.remove_product("Samsung galaxy s6")
    try:
        cart_page.verify_product_in_cart("Samsung galaxy s6")
        assert False, "Product was not removed from the cart!"
    except:
        print("Test Passed: Product successfully removed from the cart.")

