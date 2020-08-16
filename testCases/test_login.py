from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadProperties
from  utilities.customLogger import logGen
import pytest


@pytest.mark.usefixtures("setUp")
class Test_001():

    username = ReadProperties.getuserName()
    password = ReadProperties.getPwd()
    logger = logGen()

    def test_homePageTitle(self):
        self.logger.info("*************** test_homePageTitle ************")
        expected_title = "Your store. Login"
        actual_title = self.driver.title
        if actual_title == expected_title:
            assert True
            self.logger.info("Title verified successfully\n")
        else:
            self.driver.save_screenshot("./Screenshots//test_homePageTitle.png")
            self.logger.error("Title verification failed\n")
            assert False


    def test_login(self):
        self.logger.info("*************** test_login ************")
        self.lp = LoginPage(self.driver)

        self.lp.enterUserName(self.username)
        self.logger.info("Entered Username")

        self.logger.info("Entered Password")
        self.lp.enterPassword(self.password)

        self.lp.clickLogin()
        self.logger.info("Clicked on login button")

        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("Login verified successfully\n")

        else:
            self.driver.save_screenshot("./Screenshots//test_login.png")
            self.driver.close()
            self.logger.error("Login Failed\n")
            assert False







