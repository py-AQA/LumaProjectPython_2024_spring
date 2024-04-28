import os
from time import time

import allure
import allure_commons
import pytest
from faker import Faker
from selene import browser, support
from selenium import webdriver


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    cwd_report = os.path.join(os.path.dirname(os.path.abspath(__file__)), "allure-results")
    allure_dir = getattr(config.option, "allure_report_dir", None)
    if not allure_dir:
        setattr(config.option, "allure_report_dir", cwd_report)


@pytest.fixture(autouse=True)
def browser_management():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    # options.add_argument("--headless")
    if os.environ.get('PYTHONDONTWRITEBYTECODE') == '1':
        # options.add_experimental_option('prefs', {'intl.accept_languages': "en-US,en;q=0.9"}) !!!! doesn't work
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    browser.config.driver_options = options

    browser.config.timeout = 10
    # browser.config.window_width = 1920
    # browser.config.windows_height = 1080
    browser.config.reports_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "driver-report")
    # browser.config.last_page_source = "123"
    browser.config.log_outer_html_on_failure = True
    # browser.config.save_screenshot_on_failure = False
    # browser.config.save_page_source_on_failure = False

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=allure.attachment_type.PNG
    )
    browser.quit()


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


@pytest.fixture
def state():
    return Faker().state()


@pytest.fixture
def postcode():
    return Faker().postcode()


@pytest.fixture
def phone_number():
    return Faker().phone_number()


@pytest.fixture
def street_address():
    return Faker().street_address()


@pytest.fixture
def city():
    return Faker().city()
