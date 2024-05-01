import pytest
from pages.locators import SalePageLocators, BaseLocators
from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss


# @pytest.mark.xfail
# def test_011_011_001_selenium(driver):
#     # assert error !!! 'Sale' is missing
#     driver.get(SalePageLocators.LINK_WOMEN_SALE)
#     list_br = driver.find_elements(*BaseLocators.BREADCRUMBS_LIST)
#     expected_list_breadcrumbs = ['Home', 'Sale', 'Women Sale']
#     actual_list_breadcrumbs = []
#     for elem in list_br:
#         actual_list_breadcrumbs.append(elem.text)
#     assert expected_list_breadcrumbs == actual_list_breadcrumbs

@pytest.mark.xfail
def test_011_011_001_women_sale_breadcrumbs_is_correct():
    # assert error !!! 'Sale' is missing
    browser.open(SalePageLocators.LINK_WOMEN_SALE)
    ss(BaseLocators.BREADCRUMBS_LIST).should(have.texts('Home', 'Sale', 'Women Sale'))


# def test_011_011_002_selenium(driver):
#     driver.get(SalePageLocators.LINK_WOMEN_SALE)
#     breadcrumbs_links = driver.find_elements(*BaseLocators.BREADCRUMBS_LINKS)
#     links = [elem.get_attribute('href') for elem in breadcrumbs_links]
#     for elem in links:
#         driver.get(elem)
#         assert driver.current_url in SalePageLocators.BREADCRUMBS_LINKS_ON_PAGE_WOMEN_SALE
#

@pytest.mark.xfail
def test_011_011_002_breadcrumbs_redirection_from_women_sale():
    browser.open(SalePageLocators.LINK_WOMEN_SALE)
    elements = ss(BaseLocators.BREADCRUMBS_LINKS).by(have.attribute('href'))
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/sale.html']
    for i, element in enumerate(elements):
        element.should(have.attribute('href').value(expected_links[i]))


# def test_011_011_002_breadcrumbs_redirection_from_women_sale():
#     browser.open(SalePageLocators.LINK_WOMEN_SALE)
#     # breadcrumbs_links = ss(BaseLocators.BREADCRUMBS_LINKS)
#     links = ss(BaseLocators.BREADCRUMBS_LINKS).filtered_by(have.attribute('href'))
#
#     # links = [elem.get_attribute('href') for elem in breadcrumbs_links]
#     for elem in links:
#         browser.open(elem)
#         browser.should(have.url(in SalePageLocators.BREADCRUMBS_LINKS_ON_PAGE_WOMEN_SALE
# ss('.item').filtered_by(text('foo'))
# href_value = ss('a').first.attribute('href')