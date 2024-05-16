import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture()
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()

    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    request.cls.driver = driver

