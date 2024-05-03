import pytest
from selene import browser
from pages.basket_page import BasketPage
import allure
from pages.urls import main_page_link


# тестов  мало поэтому нет необходимости выносить это в фикстуру
# @pytest.fixture(scope="function")
# def open_main_page():
#     page = BasketPage(browser, main_page_link)
#     page.open()
#     return page

# def test_add_to_cart_from_main(open_main_page):
#     open_main_page.add_to_cart_from_main_page()


@allure.link('https://trello.com/c/WVaLK93g')
def test_add_to_cart_from_main():
    page = BasketPage(browser, main_page_link)
    page.open()
    page.add_to_cart_from_main_page()


@allure.link('https://trello.com/c/WVaLK93g')
def test_color_and_clickability_of_view_and_edit_cart_link_in_the_mini_cart_tc_005_001_011():
    page = BasketPage(browser, main_page_link)
    page.open()
    page.check_color_and_clickability_of_view_and_edit_cart_link_in_the_mini_cart()
    # time.sleep(5)


@allure.link('https://trello.com/c/w8Of4GYe')
def test_checking_the_link_opens_the_cart_page_tc_005_001_012():
    page = BasketPage(browser, main_page_link)
    page.open()
    page.checking_the_link_opens_the_cart_page()

# @pytest.mark.skip #  пробный искали цвет
# def test_color_button():
#     page = BasketPage(browser, main_page_link)
#     page.open()
#     page.check_color_button()
