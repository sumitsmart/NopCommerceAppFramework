from pageObjects.LoginPage import LoginPage

class Test_001:


    baseURL = "https://admin-demo.nopcommerce.com/admin/"
    username = "admin@yourstore.com"
    password = "admin"


    def test_homePageTitle(self,setUp):

        self.driver = setUp
        self.driver.get(self.baseURL)
        expected_title = "Your store. Login"
        actual_title = self.driver.title
        if actual_title == expected_title:
            assert True
        else:
            self.driver.save_screenshot("./Screenshots//test_homePageTitle.png")
            self.driver.close()
            assert False



    def test_login(self,setUp):

        self.driver = setUp
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.enterUserName(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            self.driver.save_screenshot("./Screenshots//test_login.png")
            self.driver.close()
            assert False







