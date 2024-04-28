import time

from pages.product_page import ProductPage
from pages import mini_cart, checkout_shipping, message
from pages.locators import ProductLocators as PL
from selene import browser, be, have


def test_checkout_from_mini_cart(user_email, first_name, last_name, street_address, city):
    page = ProductPage(browser, PL.RADIANT_TEE_URL)
    page.open()
    page.add_to_cart()
    page.open_mini_cart()
    mini_cart.checkout()
    # time.sleep(10)
    checkout_shipping.fill_shipping_address(user_email, first_name, last_name, street_address, city)
