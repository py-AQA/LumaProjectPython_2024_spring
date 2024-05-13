import time
import allure
import pytest
from selene import browser, be, have
# from selene.support.conditions.have import css_property
# from selene.core.query import css_property
from selene.support.shared.jquery_style import s, ss
# from selenium.webdriver import Keys
from pages.locators import ProductLocators as PL
from selenium.webdriver.support.color import Color

"================Функции OLD VERSION ПРЕНЕСЕНЫ для правильного выполнения тестов в mini_cart.py===================="


# class BasketPage(BasePage):
@pytest.mark.skip
def check_color_and_clickability_of_view_and_edit_cart_link_in_the_mini_cart():
    """ old version"""
    time.sleep(1)
    s(PL.MINI_BASKET_WINDOW).click()
    edit = s(PL.VIEW_AND_EDIT_CART_HREF)
    edit.should(have.attribute("href"))
    s('a.action').should(have.css_property("color", Color.from_string("#006bb4").rgba))
    # color = browser.element(PL.VIEW_AND_EDIT_CART_HREF).value_of_css_property("color")
    # color = browser.element(PL.VIEW_AND_EDIT_CART_HREF).should(have(css_property("color")))

    # color = s(PL.VIEW_AND_EDIT_CART_HREF).get("color")
    # color.should(have(css_property("color")))
    # s(should_have(css_property, expected_value)


@pytest.mark.skip  # Пробный тест, находили способ проверить цвет элемента
def check_color_button():
    """ old version"""
    s(PL.MINI_BASKET_WINDOW).click()
    s('a.action').should(have.css_property("color", Color.from_string("#006bb4").rgba))

    # login_button_colour = Color.from_string(browser.find_element(By.CSS_SELECTOR, 'login').value_of_css_property('color')).rgba

    # assert login_button_background_colour.hex == '#ff69b4'
    # assert login_button_background_colour.rgba == 'rgba(255, 105, 180, 1)'
    # assert login_button_background_colour.rgb == 'rgb(255, 105, 180)'

    # login_button_colour = Color.from_string(driver.find_element(By.ID, 'login').value_of_css_property('color'))
    # login_button_background_colour = Color.from_string(driver.find_element(By.ID, 'login').value_of_css_property('background-color'))


@allure.link("https://trello.com/c/lvLslLGD")
def checking_product_name_are_correct_in_checkout_cart_page():
    s(PL.NAME_ARGUS_ALL_WEATHER_TANK_CHECKOUT_CART).should(have.text("Argus All-Weather Tank"))


def checking_size_are_correct_in_checkout_cart_page():
    s(PL.SIZE_M_ARGUS_ALL_WEATHER_TANK_CHECKOUT_CART).should(have.text("M"))


def checking_color_are_correct_in_checkout_cart_page():
    s(PL.COLOR_GRAY_ARGUS_CHECKOUT_CART).should(have.text("Gray"))


@allure.link("https://trello.com/c/SQ3op4DX")
def check_price_present_in_checkout_cart_page():
    s(PL.PRICE_ITEM_CHECKOUT_CART).should(be.present).should(have.text("$22.00"))


def check_qty_present_in_checkout_cart_page():
    s(PL.QTY_FIELD_CHECKOUT_CART).should(be.present)


def check_subtotal_present_in_checkout_cart_page():
    s(PL.CART_SUBTOTAL_CHECKOUT_CART).should(be.present).should(have.text("$"))
