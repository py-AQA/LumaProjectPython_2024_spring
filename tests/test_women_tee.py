from selene.support.conditions.have import values_containing, values
from selenium.webdriver.support.expected_conditions import any_of

from pages.locators import SalePageLocators, BaseLocators

from selene.support.shared.jquery_style import s, ss
from selene.support.conditions import be, have
from selene import browser


def test_011_016_001_women_tees_breadcrumbs_is_correct(driver):
    driver.get(SalePageLocators.LINK_TEES_WOMEN)
    list_br = driver.find_elements(*BaseLocators.BREADCRUMBS_LIST)
    expected_list_breadcrumbs = ['Home', 'Women', 'Tops', 'Tees']
    actual_list_breadcrumbs = []
    for elem in list_br:
        actual_list_breadcrumbs.append(elem.text)
    assert expected_list_breadcrumbs == actual_list_breadcrumbs


def test_011_016_002_breadcrumbs_redirection_from_women_tees(driver):
    # check if all link are there
    driver.get(SalePageLocators.LINK_TEES_WOMEN)
    breadcrumb_links = driver.find_elements(*BaseLocators.BREADCRUMBS_LINKS)
    links = [elem.get_attribute('href') for elem in breadcrumb_links]
    assert links == SalePageLocators.BREADCRUMBS_LINKS_ON_PAGE_TEES


# def test_011_016_002_breadcrumbs_redirection_from_women_tees_new42():
#     browser.open(SalePageLocators.LINK_TEES_WOMEN)
#     ss(BaseLocators.BREADCRUMBS_LINKS).filtered_by(have.attribute('href')).should(
#         have.attribute('href', values_containing('https://magento.softwaretestingboard.com/',
#                               'https://magento.softwaretestingboard.com/women.html',
#                               'https://magento.softwaretestingboard.com/women/tops-women.html')))


def test_011_016_002_breadcrumbs_redirection_from_women_tees_new4():
    browser.open(SalePageLocators.LINK_TEES_WOMEN)
    elements = ss(BaseLocators.BREADCRUMBS_LINKS).filtered_by(have.attribute('href'))

    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/women.html',
                      'https://magento.softwaretestingboard.com/women/tops-women.html']

    for element in elements:
        element.should(have.attribute('href').value(any_of(*expected_links)))



def test_011_016_002_breadcrumbs_redirection_from_women_tees_new3():
    browser.open(SalePageLocators.LINK_TEES_WOMEN)
    ss(BaseLocators.BREADCRUMBS_LINKS).filtered_by(have.attribute('href')).should(
        have.texts('Home', 'Women', 'Tops'))
