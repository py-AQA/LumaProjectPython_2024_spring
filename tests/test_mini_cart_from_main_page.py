import time
import allure
from selene import browser
from pages import mini_cart
from pages.home_page import HomePage
from pages.urls import *


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
    page = HomePage(browser, main_page_link)
    page.open()
    page.add_to_cart_from_main_page()

@allure.link('https://trello.com/c/WVaLK93g')
def test_color_and_clickability_of_view_and_edit_cart_link_in_the_mini_cart_tc_005_001_011():
    page = HomePage(browser, main_page_link)
    page.open()
    page.add_to_cart_from_main_page()
    page.is_counter_number_visible()
    page.go_to_mini_cart()
    # mini_cart = BasketPage(browser, main_page_link)
    mini_cart.check_color_of_view_and_edit_cart_link_in_the_mini_cart()
    mini_cart.check_clickability_of_view_and_edit_cart_link_in_the_mini_cart()


# @pytest.mark.skip #  пробный искали цвет
# def test_color_button():
#     page = BasketPage(browser, main_page_link)
#     page.open()
#     page.check_color_button()


@allure.link('https://trello.com/c/w8Of4GYe')
def test_checking_the_link_opens_the_cart_page_tc_005_001_012():
    page = HomePage(browser, main_page_link)
    page.open()
    page.add_to_cart_from_main_page()
    page.is_counter_number_visible()
    page.go_to_mini_cart()
    mini_cart.checking_the_link_opens_checkout_cart_page()


@allure.link("https://trello.com/c/v4hVrwzq")
def test_size_color_and_product_name_are_correct_tc_005_001_013():
    page = HomePage(browser, main_page_link)
    page.open()
    page.add_to_cart_from_main_page()
    page.is_counter_number_visible()
    page.go_to_mini_cart()
    mini_cart.checking_the_size_color_and_product_name_are_correct("M", "Gray", "Argus All-Weather Tank")


@allure.link("https://trello.com/c/p6iExP1c")
def test_checking_present_price_item_and_cart_subtotal_in_the_mini_cart_tc_005_001_014():
    page = HomePage(browser, main_page_link)
    page.open()
    page.add_to_cart_from_main_page()
    page.is_counter_number_visible()
    page.go_to_mini_cart()
    mini_cart.checking_present_price_item_and_cart_subtotal_in_the_mini_cart("$22.00", "$22.00")


@allure.link("https://trello.com/c/uCZZgQks")
def test_change_quantity_of_an_item_and_changes_price_in_cart_subtotal_mini_cart_tc_005_001_015():
    page = HomePage(browser, main_page_link)
    page.open()
    page.add_to_cart_from_main_page()
    page.is_counter_number_visible()
    page.go_to_mini_cart()
    mini_cart.should_be_success_message("You added Argus All-Weather Tank to your shopping cart.")
    mini_cart.change_qty("7")
    mini_cart.should_be_quantity_change("7")
    mini_cart.should_be_change_subtotal("$22.00", "$154.00")
