import pytest
from  selenium import webdriver
from pageObjects.LoginPage import LoginPage

class TEST_001_Login:

    baseURL = "https://admin-demo.nopcommerce.com/admin/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self,setUp):

        self.driver = setUp
        self.driver.get(self.baseURL)
        expected_title = "Dashboard / nopCommerce administration"
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == expected_title:
            assert True
        else:
            assert False
        self.driver.close()


    def test_login(self,setUp):

        self.driver = setUp
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.enterUserName(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False






