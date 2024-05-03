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


# @pytest.mark.skip #  пробный искали цвет
# def test_color_button():
#     page = BasketPage(browser, main_page_link)
#     page.open()
#     page.check_color_button()


@allure.link('https://trello.com/c/w8Of4GYe')
def test_checking_the_link_opens_the_cart_page_tc_005_001_012():
    page = BasketPage(browser, main_page_link)
    page.open()
    page.checking_the_link_opens_the_cart_page()


@allure.link("https://trello.com/c/v4hVrwzq")
def test_size_color_and_product_name_are_correct_tc_005_001_013():
    page = BasketPage(browser, main_page_link)
    page.open()
    page.checking_the_size_color_and_product_name_are_correct()


@allure.link("https://trello.com/c/p6iExP1c")
def test_checking_present_price_item_and_cart_subtotal_in_the_mini_cart_tc_005_001_014():
    page = BasketPage(browser, main_page_link)
    page.open()
    page.checking_present_price_item_and_cart_subtotal_in_the_mini_cart()

def test_change_quantity_of_an_item_and_changes_price_in_cart_ubtotal_mini_cart():
    page = BasketPage(browser, main_page_link)
    page.open()
    page.change_quantity_of_an_item_and_changes_price_in_cart_ubtotal_mini_cart()