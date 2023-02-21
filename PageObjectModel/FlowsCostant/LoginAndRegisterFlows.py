import time
from selenium.webdriver.common.by import By

from PageObjectModel.FlowsCostant.Set_Dev_Mode import SetUtilDevMode
from PageObjectModel.action_app.Tap_Drag_Util import TapAndDragUtil


class LoginAndRegisterFlowsUtils:

    @staticmethod
    def ConfigEnvAndLoginUser(email, password, driver):
        SetUtilDevMode.SetDevelopMode(driver)
        # Input email, adn send email of user
        driver.find_element(By.XPATH, "//android.widget.EditText[contains(@text, 'Correo electrónico')]").send_keys(email)
        time.sleep(1)
        driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Continuar')]").click()
        # Input password, and send password of user
        driver.find_element(By.XPATH, "//android.widget.EditText[contains(@text, 'Ingresa tu contraseña')]").send_keys(password)
        # tap out the input to find the element correctly
        TapAndDragUtil.tap_screen(963, 1210, 50, driver)
        # Click in button iniciar sesion
        driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Iniciar sesión')]").click()

    @staticmethod
    def LoginUser(email, password, driver):
        # Input email, adn send email of user
        driver.find_element(By.XPATH, "//android.widget.EditText[contains(@text, 'Correo electrónico')]").send_keys(
            email)
        time.sleep(1)
        driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Continuar')]").click()
        # Input password, and send password of user
        driver.find_element(By.XPATH, "//android.widget.EditText[contains(@text, 'Ingresa tu contraseña')]").send_keys(password)
        # tap out the input to find the element correctly
        TapAndDragUtil.tap_screen(963, 1210, 50, driver)
        # Click in button iniciar sesion
        driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Iniciar sesión')]").click()



