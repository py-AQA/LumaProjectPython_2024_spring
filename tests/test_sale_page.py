from selene import browser, be, have
from pages.locators import SalePageLocators, BaseLocators


def test_availability_of_name():
    browser.open('https://magento.softwaretestingboard.com/sale.html')
    browser.element(SalePageLocators.GEAR_DEALS_TITLE).should(be.visible)


def test_availability_of_links_bags():
    browser.open('https://magento.softwaretestingboard.com/sale.html')

    browser.element(SalePageLocators.BAGS_LINK).should(be.visible)
    browser.element(SalePageLocators.FITNESS_EQUIPMENT_LINK).should(be.visible)


def test_availability_of_links_fitness():
    browser.open('https://magento.softwaretestingboard.com/sale.html')

    browser.element(SalePageLocators.FITNESS_EQUIPMENT_LINK).should(be.visible)


def test_bags_link_clickability():
    browser.open('https://magento.softwaretestingboard.com/sale.html')
    browser.element(SalePageLocators.BAGS_LINK).should(be.clickable)


def test_bags_link_correct_redirection():
    browser.open('https://magento.softwaretestingboard.com/sale.html')
    browser.element(SalePageLocators.BAGS_LINK).click()
    browser.should(have.url_containing("gear/bags"))
    browser.element(BaseLocators.PAGE_NAME).should(have.text('Bags'))


def test_fitness_link_clickability():
    browser.open('https://magento.softwaretestingboard.com/sale.html')
    browser.element(SalePageLocators.FITNESS_EQUIPMENT_LINK).click()
    browser.should(have.url_containing("gear/fitness-equipment"))
    browser.element(BaseLocators.PAGE_NAME).should(have.text('Fitness'))


def test_011_001_001_sale_breadcrumbs_is_correct(driver):
    driver.get(SalePageLocators.LINK_SALE)
    list_br = driver.find_elements(*BaseLocators.BREADCRUMBS_LIST)
    expected_list_breadcrumbs = ['Home', 'Sale']
    actual_list_breadcrumbs = []
    for elem in list_br:
        actual_list_breadcrumbs.append(elem.text)
    assert expected_list_breadcrumbs == actual_list_breadcrumbs


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
    breadcrumbs_links = browser.find_elements(*BaseLocators.BREADCRUMBS_LINKS)
    links = [elem.get_attribute('href') for elem in breadcrumbs_links]
    for elem in links:
        browser.get(elem)
        assert browser.current_url in SalePageLocators.BREADCRUMBS_LINKS_ON_PAGE_WOMEN_SALE


def test_011_016_001_women_tees_breadcrumbs_is_correct(driver):
    driver.get(SalePageLocators.LINK_TEES_WOMEN)
    list_br = browser.find_elements(*BaseLocators.BREADCRUMBS_LIST)
    expected_list_breadcrumbs = ['Home', 'Women', 'Tops', 'Tees']
    actual_list_breadcrumbs = []
    for elem in list_br:
        actual_list_breadcrumbs.append(elem.text)
    assert expected_list_breadcrumbs == actual_list_breadcrumbs


def test_011_016_002_breadcrumbs_redirection_from_women_tees(driver):
    # check if all link are there
    driver.get(SalePageLocators.LINK_TEES_WOMEN)
    breadcrumb_links = browser.find_elements(*BaseLocators.BREADCRUMBS_LINKS)
    links = [elem.get_attribute('href') for elem in breadcrumb_links]
    assert links == SalePageLocators.BREADCRUMBS_LINKS_ON_PAGE_TEES
