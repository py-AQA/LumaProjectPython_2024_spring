import pytest
from selene import browser, be, have
from selene.support.conditions.have import css_property
from selene.core.query import css_property
from selene.support.shared.jquery_style import s, ss
from pages.locators import ProductLocators as PL
from pages.base_page import BasePage
from selenium.webdriver.support.color import Color


class BasketPage(BasePage):
    def add_to_cart_from_main_page(self):
        s(PL.ARGUS_All_WEATHER_TANK_SIZE).click()
        s(PL.ARGUS_All_WEATHER_TANK_COLOR).click()
        s(PL.ARGUS_All_WEATHER_TANK_ADD_TO_CARD).click()

    def check_color_and_clickability_of_view_and_edit_cart_link_in_the_mini_cart(self):
        # добавляем функцию add_to_cart_from_main_page()
        self.add_to_cart_from_main_page()
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
    def check_color_button(self):
        self.add_to_cart_from_main_page()
        s(PL.MINI_BASKET_WINDOW).click()
        s('a.action').should(have.css_property("color", Color.from_string("#006bb4").rgba))

    # login_button_colour = Color.from_string(browser.find_element(By.CSS_SELECTOR, 'login').value_of_css_property('color')).rgba

    # assert login_button_background_colour.hex == '#ff69b4'
    # assert login_button_background_colour.rgba == 'rgba(255, 105, 180, 1)'
    # assert login_button_background_colour.rgb == 'rgb(255, 105, 180)'

    # login_button_colour = Color.from_string(driver.find_element(By.ID, 'login').value_of_css_property('color'))
    # login_button_background_colour = Color.from_string(driver.find_element(By.ID, 'login').value_of_css_property('background-color'))

    def checking_the_link_opens_the_cart_page(self):
        self.add_to_cart_from_main_page()
        s(PL.MINI_BASKET_WINDOW).click()
        s(PL.VIEW_AND_EDIT_CART_LINK).click()
