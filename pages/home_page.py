from selene.support.shared.jquery_style import s, ss
from selene import  be
from pages.base_page import BasePage
# from pages.basket_page import BasketPage
from pages.locators import NavigatorLocators as NL, ProductLocators as PL
from pages.urls import main_page_link


class HomePage(BasePage):

    def go_to_pages(self):
        self.navigate_to(NL.NAV_NEW)
        self.navigate_to(NL.NAV_WOMEN)
        self.navigate_to(NL.NAV_MEN)
        self.navigate_to(NL.NAV_GEAR)
        self.navigate_to(NL.NAV_TRAINING)
        self.navigate_to(NL.NAV_SALE)

    def navigate_to(self, locator):
        s(locator).click()

    def add_to_cart_from_main_page(self):
        s(PL.ARGUS_All_WEATHER_TANK_SIZE).click()
        s(PL.ARGUS_All_WEATHER_TANK_COLOR).click()
        s(PL.ARGUS_All_WEATHER_TANK_ADD_TO_CARD).click()

    def go_to_mini_cart(self):
        s(PL.MINI_BASKET_WINDOW).should(be.clickable).click()
