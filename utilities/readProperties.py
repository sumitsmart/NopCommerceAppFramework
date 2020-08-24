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
        chromedriver = config.get("Environment variables","chromeDriver")
        return  chromedriver

    @staticmethod
    def getGeckoDriverPath():
        geckodriver = config.get("Environment variables","geckoDriver")
        return  geckodriver



