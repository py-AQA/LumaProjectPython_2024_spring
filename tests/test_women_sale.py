import pytest
from pages.locators import SalePageLocators, BaseLocators


@pytest.mark.xfail
def test_011_011_001_women_sale_breadcrumbs_is_correct(driver):
    # assert error !!! 'Sale' is missing
    driver.get(SalePageLocators.LINK_WOMEN_SALE)
    list_br = driver.find_elements(*BaseLocators.BREADCRUMBS_LIST)
    expected_list_breadcrumbs = ['Home', 'Sale', 'Women Sale']
    actual_list_breadcrumbs = []
    for elem in list_br:
        actual_list_breadcrumbs.append(elem.text)
    assert expected_list_breadcrumbs == actual_list_breadcrumbs


def test_011_011_002_breadcrumbs_redirection_from_women_sale(driver):
    driver.get(SalePageLocators.LINK_WOMEN_SALE)
    breadcrumbs_links = driver.find_elements(*BaseLocators.BREADCRUMBS_LINKS)
    links = [elem.get_attribute('href') for elem in breadcrumbs_links]
    for elem in links:
        driver.get(elem)
        assert driver.current_url in SalePageLocators.BREADCRUMBS_LINKS_ON_PAGE_WOMEN_SALE
