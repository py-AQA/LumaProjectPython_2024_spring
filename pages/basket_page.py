from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss

from pages.locators import ProductLocators as PL
from pages.base_page import BasePage



class BasketPage(BasePage):
        def add_to_cart_from_main_page(self):
            s(PL.ARGUS_All_WEATHER_TANK_SIZE).click()
            s(PL.ARGUS_All_WEATHER_TANK_COLOR).click()
            s(PL.ARGUS_All_WEATHER_TANK_ADD_TO_CARD).click()

        def check_link_present_in_the_window_mini_cart(self):
            s(PL.MINI_BASKET_WINDOW).click()
