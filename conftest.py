import pytest
from utils.browser_factory import WebdriverFactory
from utils.config import *
import random


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    browser_name = request.param
    driver = WebdriverFactory.get_webdriver(browser_name)
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


@pytest.fixture
def open_main_page(driver):
    driver.get(BASE_URL)
    driver.maximize_window()
    return driver


@pytest.fixture()
def unique_email():
    first_name = "many"
    last_name = "mansov"
    cohort_number = "14"
    random_number = random.randint(1000, 9999)
    email_domain = "yandex.ru"
    return f"{first_name}_{last_name}_{cohort_number}_{random_number}@{email_domain}"
