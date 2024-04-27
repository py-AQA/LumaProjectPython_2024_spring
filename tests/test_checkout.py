from pages.product_page import ProductPage
from pages import mini_cart, checkout_shipping
from pages.locators import ProductLocators as PL
from selene import browser, be, have


def test_checkout_from_mini_cart():
    page = ProductPage(browser, PL.RADIANT_TEE_URL)
    page.open()
    page.add_to_cart()
    page.open_mini_cart()
    mini_cart.checkout()
    checkout_shipping.fill_shipping_address()