from selene import browser, be, have
from pages.home_page import HomePage

def test_breadcrumb_trails():

    url = "https://magento.softwaretestingboard.com"
    
    page = HomePage(browser, url)
    page.open()
    page.go_to_pages()
