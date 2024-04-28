import time

from selene import browser

from pages.basket_page import BasketPage
from pages.urls import main_page_link


def test_add_to_cart_from_main():
    page = BasketPage(browser, main_page_link)
    page.open()
    page.add_to_cart_from_main_page()


def test_check_link_present_in_the_window_mini_cart():
    page = BasketPage(browser, main_page_link)
    page.open()
    page.add_to_cart_from_main_page()
    page.check_link_present_in_the_window_mini_cart()
    time.sleep(5)
