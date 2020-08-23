import time

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadProperties
from  utilities.customLogger import logGen
import pytest
from utilities import ExcelUtility


@pytest.mark.usefixtures("setUp")
class Test_001_DDT():

    path = "./testData//LoginData.xlsx"


    logger = logGen()

    def test_loginDDT(self):
        self.logger.info("*************** test_loginDDT ************")
        self.lp = LoginPage(self.driver)
        list_status = []


        noOfRows = ExcelUtility.getRowCount(self.path,"Sheet1")
        #noOfCol = ExcelUtility.getColumnCount(self.path,"Sheet1")

        for row in range(2,noOfRows+1):
                username = ExcelUtility.readData(self.path,"Sheet1",row,1)
                password = ExcelUtility.readData(self.path,"Sheet1",row,2)
                exp_result = ExcelUtility.readData(self.path,"Sheet1",row,3)

                self.lp.enterUserName(username)
                self.logger.info("Entered Username")

                self.lp.enterPassword(password)
                self.logger.info("Entered Password")

                self.lp.clickLogin()
                self.logger.info("Clicked on login button")
                time.sleep(5)

                actual_title = self.driver.title
                expected_title = "Dashboard / nopCommerce administration"
                if actual_title == expected_title:
                    if exp_result == "Pass":
                        self.logger.info("Login verified successfully\n")
                        self.lp.clickLogout()
                        list_status.append("Pass")

                    elif exp_result == "Fail":
                        self.logger.error("Login verification Failed\n")
                        list_status.append("Failed")

                elif actual_title != expected_title:
                    if exp_result == "Pass":
                        self.logger.info("Login verification Failed\n")
                        self.lp.clickLogout()
                        list_status.append("Fail")

                    elif exp_result == "Fail":
                        self.logger.error("Login verification successful\n")
                        list_status.append("Pass")


        if "Fail" not in list_status:
            self.logger.info("*******Login DDT passed")
            assert  True
            print(list_status)

        else:
            self.logger.error("******Login DDT Failed")
            assert False












