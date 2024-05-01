import pytest
from selene.support.conditions.have import values_containing, values
from selenium.webdriver.support.expected_conditions import any_of

from pages.locators import SalePageLocators, BaseLocators
import pytest
from selene import browser, be, have, query
from selene.support.shared.jquery_style import s, ss


from selene.support.shared.jquery_style import s, ss
from selene.support.conditions import be, have
from selene import browser


def test_011_016_001_women_tees_breadcrumbs_is_correct():
    browser.open(SalePageLocators.LINK_TEES_WOMEN)
    ss(BaseLocators.BREADCRUMBS_LIST).should(have.texts('Home', 'Women', 'Tops', 'Tees'))


# def test_011_016_001_selenium(driver):
#     driver.get(SalePageLocators.LINK_TEES_WOMEN)
#     list_br = driver.find_elements(*BaseLocators.BREADCRUMBS_LIST)
#     expected_list_breadcrumbs = ['Home', 'Women', 'Tops', 'Tees']
#     actual_list_breadcrumbs = []
#     for elem in list_br:
#         actual_list_breadcrumbs.append(elem.text)
#     assert expected_list_breadcrumbs == actual_list_breadcrumbs


# def test_011_016_002_breadcrumbs_redirection_from_women_tees(driver):
#     # check if all link are there
#     driver.get(SalePageLocators.LINK_TEES_WOMEN)
#     breadcrumb_links = driver.find_elements(*BaseLocators.BREADCRUMBS_LINKS)
#     links = [elem.get_attribute('href') for elem in breadcrumb_links]
#     assert links == SalePageLocators.BREADCRUMBS_LINKS_ON_PAGE_TEES


def test_011_016_002_breadcrumbs_redirection_from_women_tees():
    # correct, already in school git
    browser.open(SalePageLocators.LINK_TEES_WOMEN)
    elements = ss(BaseLocators.BREADCRUMBS_LINKS).by(have.attribute('href'))
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/women.html',
                      'https://magento.softwaretestingboard.com/women/tops-women.html']
    for i, element in enumerate(elements):
        element.should(have.attribute('href').value(expected_links[i]))

def test_011_016_002_check_links_in_breadcrumps():
    # сравнить ссылки ожидаемые и фактические перебором по очереди
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/women.html',
                      'https://magento.softwaretestingboard.com/women/tops-women.html']
    browser.open(SalePageLocators.LINK_TEES_WOMEN)
    for i, item in enumerate(ss(BaseLocators.BREADCRUMBS_LINKS).by(have.attribute('href'))):
        assert expected_links[i] == item.get(query.attribute('href'))


@pytest.mark.xfail
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


def test_011_016_002_breadcrumbs_redirection_from_women_tees_new321():
    browser.open(SalePageLocators.LINK_TEES_WOMEN)

    elements = ss('.breadcrumbs > ul  > li > a').filtered_by(have.attribute('href'))
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/women.html',
                      'https://magento.softwaretestingboard.com/women/tops-women.html']

    for i, element in enumerate(elements):
        element.should(have.attribute('href', expected_links[i]))
