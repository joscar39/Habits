import time
import unittest
import warnings

import openpyxl
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjectModel.FlowsCostant.LoginAndRegisterFlows import LoginAndRegisterFlowsUtils
from PageObjectModel.FlowsCostant.ModalsNpsQualificate import NpsAndRatingStore
from PageObjectModel.Global_variables.Path_Data import PathAndVariablesUtil
from PageObjectModel.action_app.RequestUtils import RequestMethod
from PageObjectModel.action_app.Scroll_util import ScrollUtil
from PageObjectModel.action_app.Tap_Drag_Util import TapAndDragUtil


class MyTestBeneficios(unittest.TestCase):
    def setUp(self):
        # Inicializacion de Manejador Appium
        caps = {
            "platformName": PathAndVariablesUtil.SetUpPlatform(),
            "appium:platformVersion": PathAndVariablesUtil.SetUpVersion(),
            "appium:deviceName": PathAndVariablesUtil.SetUpDeviceName(),
            "appium:automationName": "UiAutomator2",
            "appium:appPackage": "com.habitsv2",
            "appium:appActivity": ".MainActivity",
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True
        }

        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def test_PRO01(self, newpass="Aa123456."):
        driver = self.driver
        driver.implicitly_wait(20)
        # filesheet = f"{PathAndVariablesUtil.db_path()}/recursos/RachaDiaria.xlsx"
        # wb = openpyxl.load_workbook(filesheet)
        # datos = wb["Hoja1"]
        # name = datos['A1']
        # email = datos['B1']
        # passw = datos['C1']
        name = "Joscar"
        email = "lenyn@habitsqa.ai"
        passw = "Bb123456."

        # Ejecutar endpoint para dejar al usaurio en el dia 1 de la racha diaria
        # Obtener token
        headers = None
        headers = RequestMethod.header_auth()

        # Iniciar sesion
        LoginAndRegisterFlowsUtils.ConfigEnvAndLoginUser(email, passw, driver)
        # Verificar si mostrara modal de calificar aplicacion en tienda
        NpsAndRatingStore.SkipModalRating(email, headers, driver)

        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                                  ((By.XPATH, PathAndVariablesUtil.challenge_navbar())))
        assert element.is_displayed(), "No se inicio sesion de forma correcta, nos e muestran los elementos del navbar"
        print(f"Se inicio sesion correctamente con el usuario {name}")
        #
        # abrir menu
        ScrollUtil.open_menu(driver)
        time.sleep(1)
        # Entrar al perfil selecionando icono de imagen
        profile = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView")
        profile.click()
        time.sleep(1)
        # Entrar en la opciond e cambair contraseña
        driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Contraseña')]").click()
        time.sleep(1)
        # Ingresar contraseña enlos campos
        inputs_password = driver.find_elements(By.CLASS_NAME, "android.widget.EditText")

        inputs_password[0].send_keys(newpass)
        inputs_password[1].send_keys(newpass)
        time.sleep(1)
        # Finalizar cambio de contraseña
        driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Continuar')]").click()
        time.sleep(2)
        # Regresar al menu principal
        driver.back()
        time.sleep(1)
        # Cerrar sesion
        for i in range(2):
            driver.swipe(28, 1091, 38, 671)
        time.sleep(1)
        driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Cerrar sesión')]").click()
        time.sleep(4)
        # Cerrar modal de kaychain
        TapAndDragUtil.tap_screen(563, 1108, 50, driver)
        time.sleep(2)
        # Iniciar sesion
        LoginAndRegisterFlowsUtils.ConfigEnvAndLoginUser(email, newpass, driver)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                                  ((By.XPATH, PathAndVariablesUtil.challenge_navbar())))
        assert element.is_displayed(), "No se inicio sesion de forma correcta, nos e muestran los elementos del navbar"
        print(f"Se inicio sesion correctamente con el usuario {name}, usando la contraseña {newpass}")
        # abrir menu
        ScrollUtil.open_menu(driver)
        time.sleep(1)
        # Entrar al perfil selecionando icono de imagen
        profile = None
        profile = driver.find_elements(By.CLASS_NAME, "android.widget.ImageView")
        profile[0].click()
        time.sleep(1)
        # Entrar en la opciond e cambair contraseña
        driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Contraseña')]").click()
        time.sleep(1)
        # Ingresar contraseña enlos campos
        inputs_password = None
        inputs_password = driver.find_elements(By.CLASS_NAME, "android.widget.EditText")
        inputs_password[0].send_keys(passw)
        inputs_password[1].send_keys(passw)
        time.sleep(1)
        # Finalizar cambio de contraseña
        driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Continuar')]").click()
        time.sleep(2)
