from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadProperties
from  utilities.customLogger import logGen
import pytest
from testData.LoginData import loginData


@pytest.mark.usefixtures("setUp")
class Test_001():

    logger = logGen()


    @pytest.mark.parametrize("testdata",loginData())
    def test_login(self):
        self.logger.info("*************** test_login ************")
        self.lp = LoginPage(self.driver)

        self.lp.enterUserName(self)
        self.logger.info(loginData())

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







