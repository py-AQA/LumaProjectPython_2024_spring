from selene.support.shared.jquery_style import s, ss

from pages.base_page import BasePage
from pages.locators import class SideBarLocators as SBL

class BreadCrumbs(BasePage):
    s(SBL.ITEM_HOME).click()
    