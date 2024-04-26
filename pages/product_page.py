from selene.support.shared.jquery_style import s, ss
from pages.locators import ProductLocators as PL
from pages.base_page import BasePage


class ProductPage(BasePage):
    def add_to_cart(self):
        s(PL.RADIANT_TEE_SIZE).click()
        s(PL.RADIANT_TEE_COLOR).click()
        s(PL.RADIANT_TEE_QTY).type('2')
        s(PL.ADD_TO_CART_BUTTON).click()

    def open_mini_cart(self):
        s('.showcart').click()
