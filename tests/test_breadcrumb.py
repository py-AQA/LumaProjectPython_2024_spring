from selene import browser, be, have

def test_breadcrumb_trails():

    url = "https://magento.softwaretestingboard.com"
    
    page = HomePage(browser, url)
    page.open()
    page.go_to_pages()
