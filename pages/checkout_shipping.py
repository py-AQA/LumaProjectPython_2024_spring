import pytest
from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss

from pages.user import Person
from selene.support import by

# def fill_shipping_address(user):
#     # s("").with_(timeout=10).click()
#     s('#customer-email-fieldset #customer-email').with_(timeout=30).type(user['user_email'])
#     s('[name="firstname"]').type(user.get("first_name"))
#     s('[name="lastname"]').type(user['last_name'])
#     s('[name="street[0]"]').type(user['street_address'])
#     s('[name="city"]').type(user['city'])
#     s('[name="region_id"]').press('Colorado')
#     s('[name="postcode"]').type(user['postcode'])
#     s('[name="country_id"]').press('Colorado')
#     s('[name="country_id"]').click()
#     s('[value="AI"]').click()
#     s('[name="telephone"]').type(user['phone_number'])
#     s('#checkout-shipping-method-load input').click()
#     s('.continue').click()


def fill_shipping_address_class():
    person1 = Person()
    # s("").with_(timeout=10).click()
    s('#customer-email-fieldset #customer-email').with_(timeout=30).type(person1.user_email)
    s('[name="firstname"]').type(person1.first_name)
    s('[name="lastname"]').type(person1.last_name)
    s('[name="street[0]"]').type(person1.street_address)
    s('[name="city"]').type(person1.city)
    s('[name="region_id"]').press('Colorado')
    s('[name="postcode"]').type(person1.postcode)
    s('[name="country_id"]').press('Colorado')
    s('[name="country_id"]').click()
    s('[value="AI"]').click()
    s('[name="telephone"]').type(person1.phone_number)
    s('#checkout-shipping-method-load input').should(be.clickable).click()
    s('.continue').should(be.clickable).click()
    s('.primary.checkout').should(be.visible)
    s('#billing-address-same-as-shipping-checkmo').click()
    s('.primary.checkout').should(be.clickable).click()

    # Находим выпадающий список по селектору
    # select_element = browser.s('[name="region_id"]')

    # Выбираем опцию по тексту
    # select_element.select('Option 1')

    # type(first_name)
    #
    # s('name="street[0]"').type(street_address)
    # s('name="street[0]"').type(street_address)
