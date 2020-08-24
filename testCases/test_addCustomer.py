import pytest

from pageObjects.CustomerPage import CustomerPage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import logGen
from utilities.readProperties import ReadProperties

@pytest.mark.usefixtures("setUp")
class Test_003_AddNewCustomer():

    username = ReadProperties.getuserName()
    password = ReadProperties.getPwd()
    logger = logGen()



    def test_addNewCustomer(self):
        self.logger.info("*************** test_addNewCustomer ************")
        self.lp = LoginPage(self.driver)
        self.lp.enterUserName(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login Successful******")

        self.cp = CustomerPage(self.driver)
        self.cp.clickOnCustomermenu()
        self.cp.clickOnCustomerSubMenu()
        self.cp.clickOnAddNew()
        self.cp.enterEmail("Sumit@gmail.com")
        self.cp.enterPwd("12345")
        self.cp.enterFirstName("Sumit")
        self.cp.enterLastName("Shivhare")
        self.cp.clickGender("Male")
        self.cp.enterDOB("29/07/1992")
        self.cp.enterCompanyName("EMC")
        # self.cp.enterNewsLetter("Your store name")
        # self.cp.enterCustomerRoles("Forum Moderators")
        self.cp.enterAdminComment("Testing.....")
        self.cp.clickOnSave()

