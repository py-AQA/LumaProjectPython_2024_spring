import time

import allure
import pytest
from selene import browser, be, have
from selene.support.shared.jquery_style import s

from pages import mini_cart, checkout_shipping, checkout_cart_page
from pages.home_page import HomePage
from pages.locators import ProductLocators as PL
from pages.product_page import ProductPage
from pages.urls import *


@pytest.mark.skip
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


@allure.link("https://trello.com/c/lvLslLGD")
def test_size_color_and_product_name_are_correct_in_the_checkout_cart_page_tc_005_001_016():
    page = HomePage(browser, main_page_link)
    page.open()
    page.add_to_cart_from_main_page()
    page.is_counter_number_visible()
    page.go_to_mini_cart()
    page.go_to_checkout_cart()
    checkout_cart_page.checking_product_name_are_correct_in_checkout_cart_page("Argus All-Weather Tank")
    checkout_cart_page.checking_size_are_correct_in_checkout_cart_page("M")
    checkout_cart_page.checking_color_are_correct_in_checkout_cart_page("Gray")

@allure.link("https://trello.com/c/SQ3op4DX")
def test_check_price_qty_and_cart_subtotal_present_in_checkout_cart_page_tc_005_001_017():
    page = HomePage(browser, main_page_link)
    page.open()
    page.add_to_cart_from_main_page()
    page.is_counter_number_visible()
    page.go_to_mini_cart()
    page.go_to_checkout_cart()
    checkout_cart_page.check_price_present_in_checkout_cart_page("$22.00")
    checkout_cart_page.check_subtotal_present_in_checkout_cart_page("$22.00")
    checkout_cart_page.check_qty_present_in_checkout_cart_page()
