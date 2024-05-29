import time

import allure
import pytest
from selene import be, have, command, query
from selene.support.shared.jquery_style import s
from selenium.webdriver.support.color import Color

# from selenium.webdriver import Keys
from pages.locators import ProductLocators as PL, ShoppingCart as SC

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
def check_product_name_is_correct(item_name):
    s(PL.NAME_ARGUS_ALL_WEATHER_TANK_CHECKOUT_CART).should(have.text(item_name))


def check_size_is_correct(size):
    # s(PL.SIZE_M_ARGUS_ALL_WEATHER_TANK_CHECKOUT_CART).should(have.text(size))
    s(f'//*[contains(text(),"{size}")]/../..//*[@id="shopping-cart-table"').should(have.text(size))


def check_color_is_correct(color):
    s(PL.COLOR_GRAY_ARGUS_CHECKOUT_CART).should(have.text(color))


@allure.link("https://trello.com/c/SQ3op4DX")
def check_price_present(item_price):
    s(PL.PRICE_ITEM_CHECKOUT_CART).should(be.present).should(have.text(item_price))


def check_qty():
    s(PL.QTY_FIELD_CHECKOUT_CART).should(be.present)


def check_change_qty(qty):
    s('[data-role="cart-item-qty"]').set(qty)


def update_click():
    s('[class="action update"]').click()


def delete_item():
    s('[class="action action-delete"]').click()


def item_should_not_present():
    s(PL.NAME_ARGUS_ALL_WEATHER_TANK_CHECKOUT_CART).should(be.not_.present)


def check_subtotal(subtotal):
    s(PL.CART_SUBTOTAL_CHECKOUT_CART).should(be.present).should(have.text(subtotal))


def estimate_shipping_drop():
    s(SC.ESTIMATE_SHIPPING).click()


def select_country_drop():
    s(SC.COUNTRY_SELECT_DROP)


def select_country(country):
    s(f'//*[contains(text(), "{country}")]').click()

    # 2-й способ
    # country = s(f'//option[@data-title="{country}"]').perform(command.js.scroll_into_view).click()
    # country.click()


# def select_state_region(region):
# для штатов из дроп-даун
# state = s(f'//option[@data-title="{region}"]').perform(command.js.scroll_into_view)
# state.click()
# Для input field, без дроп-даун
# s('//*[@name="region"]').type(region)


def select_state_region(region):
    # # Проверяем наличие элемента списка штатов для выбора
    # state_dropdown = s('//select[@name="state"]')

    try:
        # Если элемент списка штатов существует, выбираем штат из дропдауна
        state = s(f'option[data-title="{region}"]').with_(timeout=4).perform(command.js.scroll_into_view)
        state.click()
    except Exception:
        # Если элемент списка штатов отсутствует, вводим регион в поле ввода
        input_region = s('input[name="region"]')
        input_region.type(region)


def post_code(code):
    s('//*[@name="postcode"]').type(code)


def flat_rate_should_be_present():
    s(SC.FLAT_RATE).should(be.present)


def fixed_type_of_shipping_selected():
    s('// *[text() = "Fixed"]').click()


def check_subtotal_value_is_present_and_correct(qty, price):
    s(f'[class="control qty"] [value="{qty}"]').should(have.attribute("value").value("3"))
    s(PL.PRICE_ITEM_CHECKOUT_CART).should(have.text(price))

    # shadow_root = s('[data-role="cart-item-qty"][id="editing-view-port"]').should(have.text(qty)).get(query.text)
    # print(shadow_root)

    subtotal = s(SC.SUBTOTAL_VAlUE).should(have.text(f'${int(qty) * float(price[1:])}')).get(query.text)
    print(subtotal)
    return subtotal


def shipping_price_is_correct(fixed):
    s('[data-th="Shipping"]').should(have.text(fixed))


def check_order_total_has_the_correct_amount(subtotal, shipping_flatRate_fixed):
    order_total = s(SC.ORDER_TOTAL_VALUE).should(
        have.text(f'${float(subtotal[1:]) + float(shipping_flatRate_fixed[1:])}')).get(query.text)
    print(order_total)


def check_proceed_to_checkout_button_should_be_clickable():
    s(SC.PROCESEED_TO_CHECKOUT_BUTTON).should(be.visible).should(be.clickable)


def redirection_to_checkout_shipping_page():
    s(SC.PROCESEED_TO_CHECKOUT_BUTTON).click()
