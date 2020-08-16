from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadProperties
from  utilities.customLogger import logGen
import pytest
from utilities import ExcelUtility


@pytest.mark.usefixtures("setUp")
class Test_001_DDT():

    path = "./testData//LoginData"


    logger = logGen()

    def test_loginDDT(self):
        self.logger.info("*************** test_loginDDT ************")
        self.lp = LoginPage(self.driver)


        noOfRows = ExcelUtility.getRowCount(self.path,"Sheet1")

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







