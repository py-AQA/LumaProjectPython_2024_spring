import time

import selene
from selene.support.shared.jquery_style import s, ss
from selene import browser, be, have
from pages import mini_cart, checkout_shipping
from pages.locators import ProductLocators as PL
from pages.product_page import ProductPage
from pages.user import Person
from selene.support.conditions import *
from selene.support import by


def test_checkout_from_mini_cart():
    success_message = 'Thank you for your purchase!'
    failure_message = 'There is no fact of purchase!'
    expected_url = 'https://magento.softwaretestingboard.com/checkout/onepage/success/'

    page = ProductPage(browser, PL.RADIANT_TEE_URL)
    page.open()
    page.add_to_cart()
    page.open_mini_cart()
    mini_cart.checkout()
    checkout_shipping.fill_shipping_address_class()
    s('#registration').should(be.visible)
    s('[data-ui-id="page-title-wrapper"]').should(be.present) #присутствует на странице
    s('.base').should(be.visible)  # виден на странице
    s('[data-ui-id="page-title-wrapper"]').should(be.in_dom) #присутствует в доме
    s('[data-ui-id="page-title-wrapper"]').should(be.not_.hidden) #не скрыт на странице
    s('.base').should(have.text(success_message))
    s('[data-ui-id="page-title-wrapper"]').should(have.no.text(failure_message))
    browser.should(have.url(expected_url))
    browser.should(have.url_containing('success'))




