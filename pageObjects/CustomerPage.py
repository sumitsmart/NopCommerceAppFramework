from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageObjects.BasePage import BasePage

class CustomerPage(BasePage):

    # object repository
    lnk_CustomerMenu_xpath = "//a[@href='#']//span[text()='Customers']"
    lnk_CustomerSubMenu_xpath = "//a[@href='/Admin/Customer/List']//span[contains(text(),'Customer')]"
    btn_addNew_xpath = "//a[@href='/Admin/Customer/Create']"
    txt_email_css = "#Email"
    txt_pwd_css = "#Password"
    txt_fname_xpath = "//input[@id='FirstName']"
    txt_lnname_xpath = "//input[@id='LastName']"
    rb_genderMale_xpath = "//input[@id='Gender_Male']"
    rb_genderFemale_xpath = "//input[@id='Gender_Female']"
    txt_dob_id = "DateOfBirth"
    txtCompanyName_css = "#Company"
    txt_newzletter_xpath = "(//div[@role='listbox'])[1]"
    lstYourStoreName_xpath = "//span[contains(text(), 'Your store name')]"
    lstTestStore2_xpath = "//span[contains(text(),'Test store 2')]"
    txtCustomerRoles_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    lstRegistered_xpath = "//span[text()='Registered']"
    lstAdministrators_xpath = "//span[text()='Administrators']"
    lstForumModerators_xpath   = "//span[text()='Forum Moderators']"
    lstGuests_xpath = "//span[text()='Guests']"
    lstVendors_xpath = "//li[@class='k-button']//span[text()='Vendors']"
    drpVendorId_xpath = "//select[@id='VendorId']"
    txtAdminComment_css = "#AdminComment"
    btnSave_xpath = "//button[@name='save']"
    btnGuestsdelete_xpath = "(//ul[@id='SelectedCustomerRoleIds_taglist']/li//span[@class='k-select'])[1]"


    def __init__(self, driver):
        super().__init__(driver)

    # Actions methods

    def clickOnCustomermenu(self):
        self.driver.find_element(By.XPATH,self.lnk_CustomerMenu_xpath).click()

    def clickOnCustomerSubMenu(self):
        self.driver.find_element(By.XPATH,self.lnk_CustomerSubMenu_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btn_addNew_xpath).click()

    def enterEmail(self,email):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_email_css).send_keys(email)

    def enterPwd(self,pwd):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_pwd_css).send_keys(pwd)

    def enterFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txt_fname_xpath).send_keys(fname)

    def enterLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txt_lnname_xpath).send_keys(lname)

    def clickGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH,self.rb_genderMale_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH,self.rb_genderFemale_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.rb_genderMale_xpath).click()

    def enterDOB(self,DOB):
        self.driver.find_element(By.ID,self.txt_dob_id).send_keys(DOB)

    def enterCompanyName(self,cname):
        self.driver.find_element(By.CSS_SELECTOR,self.txtCompanyName_css).send_keys(cname)

    def enterNewsLetter(self,role):
        self.driver.find_element(By.XPATH, self.txt_newzletter_xpath).click()
        if role == "Your store name":
            self.listvalue = self.driver.find_element(By.XPATH,self.lstYourStoreName_xpath)

        elif role == "Test store 2":
            self.listvalue = self.driver.find_element(By.XPATH,self.lstTestStore2_xpath)

        self.driver.execute_script("argument[0].click();", self.listvalue)

    def enterCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txtCustomerRoles_xpath).click()
        if role == "Registered":
            self.listItem = self.driver.find_element(By.XPATH,self.lstRegistered_xpath)
        elif role == "Administrators":
            self.listItem = self.driver.find_element(By.XPATH,self.lstAdministrators_xpath)

        elif role == "Guests":
            self.driver.find_element(By.XPATH,self.btnGuestsdelete_xpath).click()
            self.listItem = self.driver.find_element(By.XPATH,self.lstGuests_xpath)

        elif role == "Vendors":
            self.listItem = self.driver.find_element(By.XPATH,self.lstVendors_xpath)

        elif role == "Forum Moderators":
            self.listItem = self.driver.find_element(By.XPATH,self.lstForumModerators_xpath)
        #self.listItem.click()
        self.driver.execute_script("argument[0].click();",self.listItem)

    def selectManagerOfVendor(self,value):
        BasePage.selectByVisisbleText(self.driver.find_element(By.XPATH,self.drpVendorId_xpath),value)

    def enterAdminComment(self,value):
         self.driver.find_element(By.CSS_SELECTOR,self.txtAdminComment_css).send_keys(value)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()





