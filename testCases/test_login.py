import time

import pytest
from  selenium import webdriver
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
            assert False
        self.driver.close()


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
            assert False
        self.driver.close()






