from selenium import webdriver
import pytest

@pytest.fixture()
def setUp():
    driver = webdriver.Chrome()
    return driver

