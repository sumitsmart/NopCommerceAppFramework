from selenium import webdriver
import pytest
from utilities.readProperties import ReadProperties
from py.xml import html



def pytest_addoption(parser):
    parser.addoption("--browser",default="chrome")


@pytest.fixture()
def setUp(request):

    browser = request.config.getoption("browser")
    if browser == "chrome":
        print("Launching test in Chrome Browser..........")
        driver = webdriver.Chrome(executable_path=ReadProperties.getChromeDriverPath())
    elif browser == "firefox":
        print("Launching test in FireFox Browser.........")
        driver = webdriver.Firefox(executable_path=ReadProperties.getGeckoDriverPath())
    elif browser == "IE":
        print("Launching test in IE Browser...........")
        print("Running test in IE driver")

    driver.get(ReadProperties.getBaseURL())
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield
    driver.quit()


############### Pytest HTML Report #############

#It is hook for adding Environment info in HTML report

def pytest_configure(config):
    config._metadata['Project Name'] = 'npCommereceApp'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Sumit Shivhare'
#
# It is hook for delete/modify Environment info on HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)






































