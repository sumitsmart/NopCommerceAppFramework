from selenium.webdriver.support.select import Select


class BasePage:

    def __init__(self,driver):
        self.driver = driver


    '''Generic Methods'''

    def selectByVisisbleText(webelement, value):
        '''This method select dropdown value based on visible text'''
        select = Select(webelement)
        select.select_by_visible_text(value)

    def selectByIndex(element, value):
        '''This method select dropdown value based on index'''
        select = Select(element)
        select.select_by_index(value)

    def selectByValue(element, value):
        '''This method select dropdown value based on value'''
        select = Select(element)
        select.select_by_value(value)

    def selectValueFromDropDownUsingSelectOption(element, value):
        '''This method select dropdown value based on visible text'''
        industry = Select(element)
        for option in industry.options:
            if option.text == value:
                option.click()
                break

    def selectValueFromDropDown(dropdownslist, value):
        '''This method select dropdown value based on visible text'''
        for option in dropdownslist:
            if option.text == value:
                option.click()
                break
        print("Element clicked")

    def selectValues(dropdownlist, value):
        '''This method is used to select jquery dropdown based on requirement'''
        if not value[0] == 'all':
            for option in dropdownlist:
                for i in range(len(value)):
                    if option.text == value[i]:
                        option.click()
                        break
        else:
            try:
                for option in dropdownlist:
                    option.click()
            except Exception as E:
                print(E)