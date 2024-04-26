from selene import browser, be, have
from ..pages.locators import ProductLocators as PL
from ..pages.product_page import ProductPage


def test_add_to_cart():
    page = ProductPage(browser, PL.RADIANT_TEE_URL)
    page.open()
    page.add_to_cart()






