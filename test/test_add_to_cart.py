from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_add_to_cart(page):
    home_page = HomePage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    home_page.open()
    home_page.navigate_to_category("Laptops")
    home_page.select_product("Sony vaio i5")
    product_page.add_to_cart()
    cart_page.open("cart.html")
    cart_page.verify_product_in_cart("Sony vaio i5")
