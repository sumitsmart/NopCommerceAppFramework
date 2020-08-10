from selenium.webdriver.common.by import By

class LoginPage():

    # defining locators(object repository)
    textbox_username_xpath = "//input[@id='Email']"
    textbox_password_id = "Password"
    button_login_xpath = "//input[@value='Log in']"
    link_logout_linktext = "Logout"


    # this costructer is capturing driver from test case and that driver will initiate the class variable
    def __init__(self,driver):
        self.driver = driver


    # performing actions on webelements
    def enterUserName(self,username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def enterPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()






