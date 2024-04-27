from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss
from web_test.assist.allure.report import step

url = "https://magento.softwaretestingboard.com/customer/account/forgotpassword/"


def visit():
    browser.open(url)


def reset(user_email):
    s("#email_address").type(user_email).press_enter()
