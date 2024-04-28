from selene.support.shared.jquery_style import s, ss

from pages.base_page import BasePage
from pages.locators import class NavigatorLocators as NL

class HomePage(BasePage):

    def go_to_pages(self):
        navigate_to(NL.NAV_NEW)
        navigate_to(NL.NAV_WOMEN)
        navigate_to(NL.NAV_MEN)
        navigate_to(NL.NAV_GEAR)
        navigate_to(NL.NAV_TRAINING)
        navigate_to(NL.NAV_SALE)

    def navigate_to(locator):
        s(locator).click()
        