from selene import browser, be, have
from pages.locators import SalePageLocators, BaseLocators


def test_add_to_cart():
    browser.open('https://magento.softwaretestingboard.com/sale.html')
    browser.element(SalePageLocators.GEAR_DEALS_TITLE).should(be.visible)





