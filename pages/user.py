from dataclasses import dataclass

from conftest import *


@dataclass
class Person:
    user_email: str = Faker().email()
    first_name: str = Faker().first_name()
    last_name: str = Faker().last_name()
    street_address: str = Faker().street_address()
    city: str = Faker().city()
    postcode: str = Faker().postcode()
    phone_number: str = Faker().phone_number()



