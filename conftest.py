from time import time
from faker import Faker
import pytest
from selene import Browser

@pytest.fixture
def first_name():
    return Faker().first_name()


@pytest.fixture
def last_name():
    return Faker().last_name()


@pytest.fixture
def user_email():
    lst = Faker().email().split("@")
    return "".join([lst[0], str(int(time())), "@", lst[1]])


@pytest.fixture
def password():
    return Faker().password()


# @pytest.fixture(scope='function', autouse=True)
# def close_browser():
#     browser = Browser()
#     yield
#     browser.quit()
