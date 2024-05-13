import time

from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver import Keys

from pages.locators import ProductLocators as PL
from selenium.webdriver.support.color import Color


def checkout():
    time.sleep(3)
    s('.viewcart').should(be.clickable)
    s('#top-cart-btn-checkout').should(be.clickable).click()


def check_color_of_view_and_edit_cart_link_in_the_mini_cart():
    s('a.action').should(have.css_property("color", Color.from_string("#006bb4").rgba))


def check_clickability_of_view_and_edit_cart_link_in_the_mini_cart():
    edit = s(PL.VIEW_AND_EDIT_CART_HREF)
    edit.should(have.attribute("href"))


def checking_the_link_opens_checkout_cart_page():
    s(PL.VIEW_AND_EDIT_CART_LINK).click()


def checking_the_size_color_and_product_name_are_correct():
    s(PL.SEE_DETAILS).click()
    s(PL.SIZE_M).should(have.text("M"))
    s(PL.COLOR_GRAY).should(have.text("Gray"))
    s(PL.NAME_ITEM).should(have.text("Argus All-Weather Tank"))


def checking_present_price_item_and_cart_subtotal_in_the_mini_cart():
    s(PL.PRICE_ITEM).should(have.text("$22.00"))
    s(PL.CART_SUBTOTAL).should(have.text("$22.00"))


def change_qty():
    s(PL.QTY_FIELD).should(be.clickable).send_keys(Keys.BACKSPACE + "7")
    s(PL.UPDATE).click()


def should_be_quantity_change():
    s(PL.QTY_FIELD).should(have.value("7"))
    time.sleep(2)


def should_be_success_message():
    s(".message-success").should(be.visible)


def should_be_change_subtotal():
    s(PL.PRICE_ITEM).should(have.text("$22.00"))
    s(PL.CART_SUBTOTAL).should(have.text("$154.00"))
