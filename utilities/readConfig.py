from configparser import RawConfigParser

config = RawConfigParser()
config.read("./configurations//config.ini")


class ReadProperties():

    @staticmethod
    def getBaseURL():
        return config.get("Environment variables","baseURL")

    @staticmethod
    def getuserName():
        username = config.get("Environment variables", "username")
        return username

    @staticmethod
    def getPwd():
      return config.get("Environment variables", "password")


    @staticmethod
    def getChromeDriverPath():
        return config.get("Environment variables","chrome_executable_path")


    @staticmethod
    def getGeckoDriverPath():
       return config.get("Environment variables","firefox_exectuable_path")


    @staticmethod
    def getLoginPageTitle():
       return config.get("Environment variables","login_pageTitle")


    @staticmethod
    def getHomePageTitle():
        return  config.get("Environment variables","home_pageTitle")



