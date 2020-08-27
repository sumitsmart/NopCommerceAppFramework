from pageObjects.LoginPage import LoginPage
from testCases.test_base import BaseTest
from utilities.readConfig import ReadProperties
from  utilities.customLogger import logGen

class Test_Login(BaseTest):

    logger = logGen()

    def test_loginPageTitle(self):
        self.logger.info("*************** test_loginPageTitle ************")
        self.lp = LoginPage(self.driver)
        title = self.lp.getLoginPageTItle()
        if title == ReadProperties.getLoginPageTitle():
            assert True
            self.logger.info("Title verified successfully\n")
        else:
            self.logger.info("Title verification failed\n")
            assert False


    def test_login(self):
        self.logger.info("*************** test_login ************")
        self.lp = LoginPage(self.driver)
        self.lp.performLogin(ReadProperties.getuserName(),ReadProperties.getPwd())
        self.logger.info("Entered username and password")
        title = self.lp.getHomePageTitle()
        if title ==  ReadProperties.getHomePageTitle():
            assert True
            self.logger.info("Login Test Passed\n")
        else:
            self.logger.info("Login Test Failed\n")
            assert False








