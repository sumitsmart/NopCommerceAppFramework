from selenium import webdriver
import pytest

@pytest.fixture()
def setUp():
    driver = webdriver.Chrome(executable_path="./Drivers//chromedriver")
    return driver

