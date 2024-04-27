from selene import browser, have, be


def test_browser_language():
    browser.open("https://manytools.org/http-html-text/browser-language/")
    browser.element("div.middlecol code").should(have.text("Your browser"))

