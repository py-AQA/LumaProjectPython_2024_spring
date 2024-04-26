
from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss

def checkout():
    s('#top-cart-btn-checkout').click()