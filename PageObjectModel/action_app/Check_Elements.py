import time

from selenium.webdriver.common.by import By


class CheckElements:
    @staticmethod
    def CheckIfTextElementIsVisible(TextOfElement, driver):
        time.sleep(1)
        search_element = None
        search_element = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
        status_of_search = False
        for se in search_element:
            if search_element[search_element.index(se)].text == str(TextOfElement):
                status_of_search = True
                break
            else:
                status_of_search = False
        return status_of_search


