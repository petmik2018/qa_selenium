import os
import pytest

from selenium import webdriver
# from selenium.webdriver.opera.options import Options as OperaOptions

DRIVERS = os.path.expanduser("~/Downloads/drivers")


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    driver = None

    if _browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver", options=options)
    elif _browser == "opera":
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")
    elif _browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver", options=options)

    if maximized:
        driver.maximize_window()

    def final():
        driver.quit()

    request.addfinalizer(final)

    return driver

