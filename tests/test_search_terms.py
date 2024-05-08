from selenium.webdriver.common.by import By

from pages.locators import SearchTermsLocators as ST
from pages.locators import BaseLocators as Base
from selene import browser, be, have, query
from selene.support.shared.jquery_style import s, ss


def test_015_001_001_search_terms_title_is_visible():
    browser.open(ST.LINK_SEARCH_TERMS)
    s(Base.PAGE_TITLE).should(have.text("Popular Search Terms"))


# def test_015_001_001_selenium(driver):
#     driver.get(ST.LINK_SEARCH_TERMS)
#     expected_title = "Popular Search Terms"
#     actual_title = driver.find_element(*Base.PAGE_TITLE).text
#     assert expected_title == actual_title, "Page title is not correct"


def test_015_001_002_count_search_terms():
    browser.open(ST.LINK_SEARCH_TERMS)
    ss(ST.TERMS_FOR_SEARCH_LIST_QTY).should(have.size(100))


# def test_015_001_002_selenium(driver):
#     driver.get(ST.LINK_SEARCH_TERMS)
#     q_of_goods = len(driver.find_elements(*ST.TERMS_FOR_SEARCH_LIST_QTY))
#     assert q_of_goods == 100, "Nr of search terms is not equal to 100"


def test_015_001_003_check_if_search_terms_has_size_from_76_till_136():
    # assert from selenium - how to check sizes
    browser.open(ST.LINK_SEARCH_TERMS)
    list_font_sizes = []
    terms = ss(ST.LIST_OF_SEARCH_TERMS)
    for g in terms:
        g_font, g_size = g.get(query.attribute("style")).split(": ")
        g_size = float(g_size.replace("%;", ""))
        list_font_sizes.append(g_size)
    assert min(list_font_sizes) <= 76 and max(list_font_sizes) >= 136, "Font sizes not between 76 and 136"


def test_015_001_003_check_if_search_terms_has_size_from_76_till_136_selenium(driver):
    driver.get(ST.LINK_SEARCH_TERMS)
    list_font_sizes = []
    terms = driver.find_elements(By.CSS_SELECTOR, ST.LIST_OF_SEARCH_TERMS)
    for g in terms:
        g_font, g_size = g.get_attribute("style").split(": ")
        g_size = float(g_size.replace("%;", ""))
        list_font_sizes.append(g_size)
    assert min(list_font_sizes) <= 76 and max(list_font_sizes) >= 136, "Font sizes not between 76 and 136"
    # sizes_sorted = sorted(list_font_sizes)
    # assert sizes_sorted[0] != sizes_sorted[-1], "Search terms has the same size"
    # sizes_sorted = sorted(list_font_sizes)
    # assert sizes_sorted[0] != sizes_sorted[-1], "Search terms has the same size"


def test_015_001_004_check_if_5_search_terms_is_bigger(driver):
    driver.get(ST.LINK_SEARCH_TERMS)
    list_font_sizes = []
    terms = driver.find_elements(By.CSS_SELECTOR, ST.LIST_OF_SEARCH_TERMS)
    for g in terms:
        g_font, g_size = g.get_attribute("style").split(": ")
        g_size = float(g_size.replace("%;", ""))
        list_font_sizes.append(g_size)
    sizes_sorted = sorted(list_font_sizes, reverse=True)
    for size in range(0, 5):
        if sizes_sorted[size] < 88:
            assert False, "List of search terms has not 5 elements which size is bigger than 88%"


def test_015_001_005_check_if_specified_words_is_bigger_than_88(driver):
    words = ["HOODIE", "jacket", "pants", "shirt"]
    driver.get(ST.LINK_SEARCH_TERMS)
    list_of_goods = []
    list_font_sizes = []
    print()
    terms = driver.find_elements(By.CSS_SELECTOR, ST.LIST_OF_SEARCH_TERMS)
    for g in terms:
        if g.text in words:
            list_of_goods.append(g.text)
            g_font, g_size = g.get_attribute("style").split(": ")
            g_size = g_size.replace("%;", "")
            g_size = float(g_size)
            list_font_sizes.append(g_size)
    print(list_of_goods)
    print(list_font_sizes)
    assert set(list_of_goods) == set(words) and all(
        [size > 88 for size in list_font_sizes]), "Selected words have font size bigger thjan 88%"


def test_015_001_005_check_if_specified_words_is_bigger_than_88_selenium(driver):
    words = ["HOODIE", "jacket", "pants", "shirt"]
    driver.get(ST.LINK_SEARCH_TERMS)
    list_of_goods = []
    list_font_sizes = []
    print()
    terms = driver.find_elements(By.CSS_SELECTOR, ST.LIST_OF_SEARCH_TERMS)
    for g in terms:
        if g.text in words:
            list_of_goods.append(g.text)
            g_font, g_size = g.get_attribute("style").split(": ")
            g_size = g_size.replace("%;", "")
            g_size = float(g_size)
            list_font_sizes.append(g_size)
    print(list_of_goods)
    print(list_font_sizes)
    assert set(list_of_goods) == set(words) and all(
        [size > 88 for size in list_font_sizes]), "Selected words have font size bigger thjan 88%"


def test_015_001_006_check_if_search_terms_are_sorted():
    # список ключевых,вытаскиваемых с помощью selene, выглядит не так, как при selenium.
    # Теперь есть лишние пробелы, перевод строки, слова с малой буквы неправильно сортируются.
    # С selenium тест = ОК
    browser.open(ST.LINK_SEARCH_TERMS)
    list_of_goods = []  # good : strip, lower, no spaces
    list_of_goods0 = []  # words from terms applied lower()
    terms = ss(ST.LIST_OF_SEARCH_TERMS)
    for keyword in terms:
        keyword = keyword.get(query.attribute("text")).strip().replace(" ","").lower()
        list_of_goods0.append(keyword.lower())
        list_of_goods.append(keyword)
    print(list_of_goods0)
    print(list_of_goods)
    print(sorted(list_of_goods))
    list_of_goods_sorted = sorted(list_of_goods)
    assert list_of_goods0 == list_of_goods_sorted


# def test_015_001_006_check_if_search_terms_are_sorted_selenium(driver):
#     driver.get(ST.LINK_SEARCH_TERMS)
#     list_of_goods = []
#     terms = ss(ST.LIST_OF_SEARCH_TERMS)
#     for g in terms:
#         list_of_goods.append(g.text)
#     sorted_list = sorted(list_of_goods)
#     assert list_of_goods == sorted_list, "Goods are not sorted from A to Z"