import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SetUtilDevMode:
    @staticmethod
    def SetDevelopMode(driver):  # Configurar app en el entorno Develop
        driver.implicitly_wait(20)
        i = None
        for i in range(1, 11):
            driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Bienvenido a Habits 👋')]").click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located
                                        ((By.XPATH, "//android.widget.TextView[contains(@text,"
                                                    "'Bienvenido administrador.')]")))
        driver.find_element(By.XPATH, "//android.widget.EditText[contains(@text, 'Ingresa tu contraseña')]").send_keys(
            "12345678")
        time.sleep(1)
        driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Continuar')]").click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located
                                        ((By.XPATH, "//android.widget.TextView[contains(@text,"
                                                    "'Selecciona un ambiente.')]")))
        driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Desarrollo')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Finalizar')]").click()
        time.sleep(1)

    @staticmethod
    def SetDebuggMode(driver):  # Configurar app en el entorno Personalizado para debuggear long de endpoint
        driver.implicitly_wait(20)
        i = None
        for i in range(1, 11):
            driver.find_element(By.XPATH,
                                "//android.widget.TextView[contains(@text, 'Bienvenido a Habits 👋')]").click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located
                                        ((By.XPATH, "//android.widget.TextView[contains(@text,"
                                                    "'Bienvenido administrador.')]")))
        driver.find_element(By.XPATH, "//android.widget.EditText[contains(@text, 'Ingresa tu contraseña')]").send_keys(
            "12345678")
        time.sleep(1)
        driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Continuar')]").click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located
                                        ((By.XPATH, "//android.widget.TextView[contains(@text,"
                                                    "'Selecciona un ambiente.')]")))

        driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Otro (Personalizado)')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Finalizar')]").click()
        time.sleep(1)
