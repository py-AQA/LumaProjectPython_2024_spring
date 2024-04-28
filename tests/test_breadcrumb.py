from selene import browser

from pages.home_page import HomePage


def test_breadcrumb_trails():
    url = "https://magento.softwaretestingboard.com"

    page = HomePage(browser, url)
    page.open()
    page.go_to_pages()
