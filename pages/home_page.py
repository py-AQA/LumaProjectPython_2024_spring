from selene.support.shared.jquery_style import s, ss

from pages.base_page import BasePage
from pages.locators import NavigatorLocators as NL

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
        