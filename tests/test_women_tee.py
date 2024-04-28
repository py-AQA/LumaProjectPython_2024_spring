from pages.locators import SalePageLocators, BaseLocators


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
