from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    capabilities = options.to_capabilities()
    browser = webdriver.Chrome(desired_capabilities=capabilities)

    yield browser

    print("\nquit browser..")
    browser.quit()
