from configparser import RawConfigParser

config = RawConfigParser()
config.read("./configurations//config.ini")


class ReadProperties():

    @staticmethod
    def getBaseURL():
        baseURL = config.get("Environment variables","baseURL")
        return baseURL

    @staticmethod
    def getuserName():
        username = config.get("Environment variables", "username")
        return username

    @staticmethod
    def getPwd():
        pwd = config.get("Environment variables", "password")
        return pwd

    @staticmethod
    def getChromeDriverPath():
        chromedriver = config.get("Environment variables","chrome_executable_path")
        return  chromedriver

    @staticmethod
    def getGeckoDriverPath():
        geckodriver = config.get("Environment variables","firefox_exectuable_path")
        return  geckodriver

    @staticmethod
    def getLoginPageTitle():
        title = config.get("Environment variables","login_pageTitle")
        return title

    @staticmethod
    def getHomePageTitle():
        return  config.get("Environment variables","home_pageTitle")



