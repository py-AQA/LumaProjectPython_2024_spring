from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss


class SalePageLocators:
    LINK_SALE = "https://magento.softwaretestingboard.com/sale.html"
    LINK_WOMEN_SALE = "https://magento.softwaretestingboard.com/promotions/women-sale.html"
    LINK_TEES_WOMEN = "https://magento.softwaretestingboard.com/women/tops-women/tees-women.html"

    BREADCRUMBS_LINKS_ON_PAGE_TEES = ['https://magento.softwaretestingboard.com/',
                                      'https://magento.softwaretestingboard.com/women.html',
                                      'https://magento.softwaretestingboard.com/women/tops-women.html']
    BREADCRUMBS_LINKS_ON_PAGE_WOMEN_SALE = ['https://magento.softwaretestingboard.com/',
                                            'https://magento.softwaretestingboard.com/sale.html']


class BaseLocators:
    BREADCRUMBS_LIST = ".breadcrumbs li"
    BREADCRUMBS_LINKS = '.breadcrumbs > ul  > li > a'


class SearchTermsLocators:
    LINK_SEARCH_TERMS = "https://magento.softwaretestingboard.com/search/term/popular/"
    TERMS_FOR_SEARCH_LIST_QTY = '[class="item"]'
    LIST_OF_SEARCH_TERMS = '[class="item"] a'


def test_015_001_003_check_if_search_terms_has_size_from_76_till_136(driver):
    driver.get(SearchTermsLocators.LINK_SEARCH_TERMS)
    list_font_sizes = []
    terms = driver.find_elements(*SearchTermsLocators.LIST_OF_SEARCH_TERMS)
    for g in terms:
        g_font, g_size = g.get_attribute("style").split(": ")
        g_size = float(g_size.replace("%;", ""))
        list_font_sizes.append(g_size)
    assert min(list_font_sizes) <= 76 and max(list_font_sizes) >= 136, "Font sizes not between 76 and 136"


def test_015_001_004_check_if_5_search_terms_is_bigger(driver):
    driver.get(SearchTermsLocators.LINK_SEARCH_TERMS)
    list_font_sizes = []
    terms = driver.find_elements(*SearchTermsLocators.LIST_OF_SEARCH_TERMS)
    for g in terms:
        g_font, g_size = g.get_attribute("style").split(": ")
        g_size = float(g_size.replace("%;", ""))
        list_font_sizes.append(g_size)
    sizes_sorted = sorted(list_font_sizes, reverse=True)
    for size in range(0, 5):
        if sizes_sorted[size] < 88:
            assert False, "List of search terms has not 5 elements which size is bigger than 88%"


def test_015_001_006_check_if_search_terms_are_sorted():
    browser.open(SearchTermsLocators.LINK_SEARCH_TERMS)
    list_of_goods = []
    terms = ss(SearchTermsLocators.LIST_OF_SEARCH_TERMS).get()
    for g in terms:
        list_of_goods.append(g.text)
    sorted_list = sorted(list_of_goods)
    assert list_of_goods == sorted_list, "Goods are not sorted from A to Z"


def test_011_016_002_breadcrumbs_redirection_from_women_tees(driver):
    # check if all link are there
    driver.get(SalePageLocators.LINK_TEES_WOMEN)
    breadcrumb_links = driver.find_elements(*BaseLocators.BREADCRUMBS_LINKS)
    links = [elem.get_attribute('href') for elem in breadcrumb_links]
    assert links == SalePageLocators.BREADCRUMBS_LINKS_ON_PAGE_TEES
