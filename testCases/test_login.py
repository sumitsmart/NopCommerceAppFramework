from pageObjects.LoginPage import LoginPage
from testCases.test_base import BaseTest
from utilities.readProperties import ReadProperties
from  utilities.customLogger import logGen




class Test_Login(BaseTest):

    logger = logGen()

    def test_loginPageTitle(self):
        self.logger.info("*************** test_loginPageTitle ************")
        self.lp = LoginPage(self.driver)
        title = self.lp.getLoginPageTItle()
        if title == ReadProperties.getLoginPageTitle():
            self.logger.info("Title verified successfully\n")
        else:
            self.logger.info("Title verification failed\n")


    def test_login(self):
        self.logger.info("*************** test_login ************")
        self.lp = LoginPage(self.driver)
        self.lp.performlogin(ReadProperties.getuserName(),ReadProperties.getPwd())
        self.logger.info("Entered username and password")
        title = self.lp.getHomePageTitle()
        assert title == ReadProperties.getHomePageTitle()
        self.logger.info("Verified Title")








