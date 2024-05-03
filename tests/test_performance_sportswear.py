import pytest
from selene.support.conditions.have import values_containing, values
from selenium.webdriver.common.by import By

from pages.locators import PerformanceSportswear, BaseLocators
from selene import browser, be, have, query
from selene.support.shared.jquery_style import s, ss
from selene.support.conditions import be, have


def test_006_008_001_visibility_of_price_photo_name():
    # I can't count elements on the page via selen
    browser.open(PerformanceSportswear.LINK_SPORT)
    ss(BaseLocators.PRODUCT_NAME).should(have.size(5))
    ss(BaseLocators.PRODUCT_PRICE).should(have.size(5))
    ss(BaseLocators.PRODUCT_IMAGE).should(have.size(5))


def test_006_008_001_visibility_of_price_photo_name_selenium(driver):
    # I have to find actual nr of elements on the page via python/selenium
    browser.open(PerformanceSportswear.LINK_SPORT)
    driver.get(PerformanceSportswear.LINK_SPORT)
    nr_of_items_on_page = len(driver.find_elements(By.CSS_SELECTOR, BaseLocators.PRODUCT_ITEM_IN_CATALOG))
    ss(BaseLocators.PRODUCT_NAME).should(have.size(nr_of_items_on_page))
    ss(BaseLocators.PRODUCT_PRICE).should(have.size(nr_of_items_on_page))
    ss(BaseLocators.PRODUCT_IMAGE).should(have.size(nr_of_items_on_page))

