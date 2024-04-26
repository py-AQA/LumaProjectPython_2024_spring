from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss

def fill_shipping_address(user_email, first_name, last_name, street_address, city):
    s('#customer-email-fieldset #customer-email').type(user_email)
    s('[name="firstname"]').type(first_name)
    s('[name="lastname"]').type(last_name)
    s('[name="street[0]"]').type(street_address)
    s('[name="city"]').type(city)

    # Находим выпадающий список по селектору
    select_element = browser.s('[name="region_id"]')

    # Выбираем опцию по тексту
    select_element.select('Option 1')
    s('[name="firstname"]').type(first_name)
    s('name="lastname"').type(last_name)
    s('name="street[0]"').type(street_address)
    s('name="street[0]"').type(street_address)
