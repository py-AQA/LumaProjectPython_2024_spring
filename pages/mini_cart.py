import time

from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss


def checkout():
    time.sleep(3)
    s('.viewcart').should(be.clickable)
    s('#top-cart-btn-checkout').should(be.clickable).click()
