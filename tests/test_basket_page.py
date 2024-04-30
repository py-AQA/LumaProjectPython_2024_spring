import time

import pytest
from selene import browser
from pages.basket_page import BasketPage
import allure
from pages.urls import main_page_link


@allure.link('https://trello.com/c/WVaLK93g')
def test_add_to_cart_from_main():
    page = BasketPage(browser, main_page_link)
    page.open()
    page.add_to_cart_from_main_page()

@allure.link('https://trello.com/c/WVaLK93g')
def test_color_and_clickability_of_View_and_edit_cart_link_in_the_mini_cart_tc_005_001_011():
    page = BasketPage(browser, main_page_link)
    page.open()
    page.check_color_and_clickability_of_View_and_edit_cart_link_in_the_mini_cart()

    time.sleep(5)
    browser.quit()


def test_Checking_hat_the_link_opens_the_cart_page_tc_005_001_012():
    page = BasketPage(browser, main_page_link)
    page.open()
    page.Checking_hat_the_link_opens_the_cart_page()

@pytest.mark.skip
def test_color_button():
    page = BasketPage(browser, main_page_link)
    page.open()
    page.check_color_button()