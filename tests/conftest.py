import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import utilities.custom_logger as cl
import logging

log = cl.customLogger(logging.DEBUG)

@pytest.fixture()
def setUp():
    log.info("Running method level setup")
    yield
    log.info("Running method level teardown")

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser="chrome"):
    log.info("Running one time setup")
    driver = None
    baseURL = "https://courses.letskodeit.com/practice"
    browser = browser.lower()
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(baseURL)
        log.info("Running tests on Chrome")
    elif browser == "firefox":
        baseURL = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get(baseURL)
        log.info("Running tests on Firefox")
    else:
        log.info("Sorry! Browser not supported.")

    if request.cls is not None:
        request.cls.driver = driver

    driver.maximize_window()
    driver.implicitly_wait(3)

    yield driver
    log.info("Running one time teardown")
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
