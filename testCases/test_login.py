from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadProperties
from  utilities.customLogger import LogGen
class Test_001:

    baseURl = ReadProperties.getBaseURL()
    username = ReadProperties.getuserName()
    password = ReadProperties.getPwd()
    logger = LogGen.loggen()

    def test_homePageTitle(self,setUp):

        self.logger.info("*************** test_homePageTitle ************")
        self.driver = setUp
        self.driver.get(self.baseURl)
        expected_title = "Your store. Login"
        actual_title = self.driver.title
        if actual_title == expected_title:
            assert True
            self.driver.close()
            self.logger.info("Title verified successfully")
        else:
            self.driver.save_screenshot("./Screenshots//test_homePageTitle.png")
            self.logger.error("Title verification failed")
            self.driver.close()
            assert False




    def test_login(self,setUp):

        self.logger.info("*************** test_login ************")
        self.driver = setUp
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURl)
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
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots//test_login.png")
            self.driver.close()
            self.logger.error("Test case failed")
            assert False







