import collections
import unittest
import time
import warnings

import allure
import numpy.random
import json
import requests
import openpyxl as xl
import openpyxl

from datetime import datetime
from datetime import timedelta

from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjectModel.FlowsCostant.LoginAndRegisterFlows import LoginAndRegisterFlowsUtils
from PageObjectModel.FlowsCostant.ModalsNpsQualificate import NpsAndRatingStore
from PageObjectModel.Global_variables.Path_Data import PathAndVariablesUtil
from PageObjectModel.action_app.Element_Constant import ElementConstantUtil
from PageObjectModel.action_app.Scroll_util import ScrollUtil
from PageObjectModel.action_app.Tap_Drag_Util import TapAndDragUtil

ngrok_ruta = "https://4dd2-200-26-185-247.ngrok.io"


class MyTestChats(unittest.TestCase):
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


    def test_act01(self):
        # Acceder a una actividad y contestarla y corroborar que se muestra la
        # actividad como pendiente de aprobacion en el historial de puntos
        driver = self.driver

        filesheet = f"{PathAndVariablesUtil.db_path()}/recursos/UserSinDataSincronizada.xlsx"
        wb = openpyxl.load_workbook(filesheet)
        datos = wb["Hoja1"]
        email = datos['B1']
        passw = datos['C1']
        name = datos['A1']
        name1 = datos['A2']
        name2 = datos['A3']
        name3 = datos['A4']

        LoginAndRegisterFlowsUtils.ConfigEnvAndLoginUser(email.value, passw.value, driver)
        # Verificar si mostrara modal de calificar aplicacion en tienda
        NpsAndRatingStore.SkipModalRating(email.value, driver)

        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                                  ((By.XPATH, PathAndVariablesUtil.challenge_navbar())))
        assert element.is_displayed(), "No se inicio sesion de forma correcta, nos e muestran los elementos del navbar"
        print("Se inicio sesion correctamente")
        # ScrollUtil.swipe_up_large(2, driver)
        # go to challenge module
        driver.find_element(By.XPATH, PathAndVariablesUtil.challenge_navbar()).click()
        time.sleep(1)
        driver.swipe(925, 1397, 862, 1397)
        time.sleep(1)
        search_activities = driver.find_elements(By.XPATH,
                                                 "//android.widget.TextView[contains(@text, 'HACER ACTIVIDAD')]")
        hile = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")

        for i in range(0, 3):
            search_activities[i].click()
            if i == 0:
                position_activity = 28
            elif i == 1:
                position_activity = 34
            else:
                position_activity = 40
            time.sleep(1)
            ScrollUtil.swipe_up_large(1, driver)
            time.sleep(1)
            element_its_not_read = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
            if element_its_not_read[-1].text == "Leer Ahora":
                driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Omitir')]").click()
                print("Se omitio la actividad de lectura")
                time.sleep(3)
            elif element_its_not_read[-1].text == "Tomar foto":
                xt_element = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
                for xt in xt_element:
                    if (xt_element[xt_element.index(xt)].text == "Paso 1") and (
                            xt_element[(xt_element.index(xt) + 1)].text == "Paso 2"):
                        print("Actividad de foto de 2 pasos")
                        # Cargar imagen del paso 1
                        xt_element[12].click()
                        time.sleep(1)
                        TapAndDragUtil.tap_screen(879, 1931, 50, driver)
                        try:
                            allow_bottom_permi = WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]")))
                            allow_bottom_permi.click()
                        except:
                            print("Los permisos de acceso a multimedia ya fueron otorgados")
                        # Seleccionar imagen
                        try:
                            driver.find_element(By.XPATH,
                                                "//android.widget.CompoundButton[contains(@text,'Imágenes')]").click()
                        except:
                            driver.find_element(By.XPATH,
                                                "//android.widget.CompoundButton[contains(@text,'Esta semana')]").click()
                        time.sleep(1)
                        search_img = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
                        for img in search_img:
                            if ("IMG" or ".jpg") in search_img[search_img.index(img)].text:
                                search_img[search_img.index(img)].click()
                                time.sleep(1)
                                break
                        ScrollUtil.swipe_up_short(1, driver)
                        finish_activities = driver.find_element(By.XPATH,
                                                                "//android.widget.TextView[contains(@text, 'Continuar')]")
                        finish_activities.click()
                        # CArgar texto del paso 2
                        input_text = driver.find_elements(By.CLASS_NAME, "android.widget.EditText")
                        for inp in input_text:
                            if input_text[input_text.index(inp)].text == "Escribe tu texto aquí":
                                input_text[input_text.index(inp)].send_keys(
                                    "Mensaje de actividad para entrar en revision")
                                break

                        send_activity = driver.find_element(By.XPATH,
                                                            "//android.widget.TextView[contains(@text, 'Enviar actividad')]")
                        send_activity.click()
                        xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
                        finish_activity = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
                            (By.XPATH, xpath)))
                        finish_activity.click()
                        time.sleep(2)
                        status_Activity = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
                        final_activity = status_Activity[position_activity].text
                        list_status = ["Por evaluar", "VER ACTIVIDAD", "Aprobado", "No aprobado"]
                        assert final_activity in list_status, "Error No se Realizo la actividad"
                        print(f"Actividad realizada exitosamente con status {status_Activity[position_activity].text}")
                        break
                    elif (xt_element[xt_element.index(xt)].text == "Paso 1") and (
                            xt_element[(xt_element.index(xt) + 1)].text != "Paso 2"):
                        print("Actividad de foto de 1 paso")
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView[1]").click()
                        time.sleep(1)
                        TapAndDragUtil.tap_screen(879, 1931, 50, driver)
                        try:
                            allow_bottom_permi = WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]")))
                            allow_bottom_permi.click()
                        except:
                            print("Los permisos de acceso a multimedia ya fueron otorgados")
                        # Seleccioanr imagen
                        try:
                            driver.find_element(By.XPATH,
                                                "//android.widget.CompoundButton[contains(@text,'Imágenes')]").click()
                        except:
                            driver.find_element(By.XPATH,
                                                "//android.widget.CompoundButton[contains(@text,'Esta semana')]").click()
                        time.sleep(1)
                        search_img = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
                        for img in search_img:
                            if ("IMG-" or ".jpg") in search_img[search_img.index(img)].text:
                                search_img[search_img.index(img)].click()
                                time.sleep(1)
                                break
                        ScrollUtil.swipe_up_short(1, driver)
                        finish_activities = driver.find_element(By.XPATH,
                                                                "//android.widget.TextView[contains(@text, 'Continuar')]")
                        finish_activities.click()
                        xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
                        finish_activity = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
                            (By.XPATH, xpath)))
                        finish_activity.click()
                        time.sleep(2)
                        status_Activity = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
                        final_activity = status_Activity[position_activity].text
                        list_status = ["Por evaluar", "VER ACTIVIDAD", "Aprobado", "No aprobado"]
                        assert final_activity in list_status, "Error No se Realizo la actividad"
                        print(f"Actividad realizada exitosamente con status {status_Activity[position_activity].text}")
                        break
                break

            elif element_its_not_read[-1].text == "Enviar actividad":
                time.sleep(1)
                text_element = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
                for text in text_element:
                    if (text_element[text_element.index(text)].text == "Paso 1") and (
                            text_element[(text_element.index(text) + 1)].text == "Paso 1: Escribe aquí:"):
                        print("Actividad de escritura")
                        input_text = driver.find_elements(By.CLASS_NAME, "android.widget.EditText")
                        for inp in input_text:
                            if input_text[input_text.index(inp)].text == "Escribe tu texto aquí":
                                input_text[input_text.index(inp)].send_keys(
                                    "Mensaje de actividad para entrar en revision")
                                break

                        send_activity = driver.find_element(By.XPATH,
                                                            "//android.widget.TextView[contains(@text, 'Enviar actividad')]")
                        send_activity.click()
                        xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
                        finish_activity = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
                            (By.XPATH, xpath)))
                        finish_activity.click()
                        time.sleep(2)
                        status_Activity = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
                        final_activity = status_Activity[position_activity].text
                        list_status = ["Por evaluar", "VER ACTIVIDAD", "Aprobado", "No aprobado"]
                        print(final_activity)
                        assert final_activity in list_status, "Error No se Realizo la actividad"
                        print(f"Actividad realizada exitosamente con status {status_Activity[position_activity].text}")
                        break
                    elif (text_element[text_element.index(text)].text == "Paso 1") and (
                            text_element[(text_element.index(text) + 1)].text != "Paso 1: Escribe aquí:"):
                        # LA actividad es de tipo video
                        print("Actividad de ver video")
                        play_video = driver.find_elements(By.CLASS_NAME, "android.widget.ImageView")
                        play_video[-1].click()
                        counter = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
                        WebDriverWait(driver, 60).until(EC.presence_of_element_located(
                            (By.XPATH, counter)))
                        timer = 0
                        while timer <= 76:
                            percentage = driver.find_element(By.XPATH, counter).text
                            total_percentage = percentage.split(sep='%')
                            timer = int(total_percentage[0])
                        close_class = driver.find_element(By.XPATH,
                                                          "//android.widget.TextView[contains(@text, 'Terminar')]")
                        close_class.click()
                        xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
                        finish_activity = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
                            (By.XPATH, xpath)))
                        finish_activity.click()
                        time.sleep(2)
                        status_Activity = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
                        final_activity = status_Activity[position_activity].text
                        list_status = ["Por evaluar", "VER ACTIVIDAD", "Aprobado", "No aprobado"]
                        assert final_activity in list_status, "Error No se Realizo la actividad"
                        print(f"Actividad realizada exitosamente con status {status_Activity[position_activity].text}")
                        break
                break
            else:
                print("Actividad no reconocida")
                driver.get_screenshot_as_file(
                    f"{PathAndVariablesUtil.evidence_path()}\\recursos\\screenshots\\Actividades"
                    "\\ACT01_Actividad no reconocida.png")

    def test_act02(self):
        # Omitir 3 veces una misma actividad. en la cuarta iteracion debera mostrar una
        # alerta indicando que se llego al limite de omisiones por dia
        driver = self.driver

        filesheet = f"{PathAndVariablesUtil.db_path()}/recursos/UserSinDataSincronizada.xlsx"
        wb = openpyxl.load_workbook(filesheet)
        datos = wb["Hoja1"]
        email = datos['B1']
        passw = datos['C1']
        name = datos['A1']
        name1 = datos['A2']
        name2 = datos['A3']
        name3 = datos['A4']

        LoginAndRegisterFlowsUtils.ConfigEnvAndLoginUser(email.value, passw.value, driver)
        # Verificar si mostrara modal de calificar aplicacion en tienda
        NpsAndRatingStore.SkipModalRating(email.value, driver)

        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                                  ((By.XPATH, PathAndVariablesUtil.challenge_navbar())))
        assert element.is_displayed(), "No se inicio sesion de forma correcta, nos e muestran los elementos del navbar"
        print("Se inicio sesion correctamente")
        # ScrollUtil.swipe_up_large(2, driver)
        # go to challenge module
        driver.find_element(By.XPATH, PathAndVariablesUtil.challenge_navbar()).click()
        time.sleep(1)
        titles = ["empty"]  # List of title by each activity
        activity_change = [False]  # Status to know if activity chance correctly
        for i in range(0, 3):
            time.sleep(1)
            search_activities = None
            title_activities = None
            search_activities = driver.find_elements(By.XPATH,
                                                     "//android.widget.TextView[contains(@text, 'HACER ACTIVIDAD')]")
            search_activities[0].click()
            time.sleep(2)
            title_activities = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
            if i == 0:  # First activity, teh status is True
                titles.append(title_activities[3].text)
                print(f"Titulo de la actividad {i + 1} es: ", titles[i])
                driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Omitir']").click()
                activity_change.append(True)  # first activity, because the status is True
                time.sleep(2)
            elif i < 2:  # If the others activities is not the firts, evaluate if the title is different from the first
                if titles[-1] != title_activities[3].text:
                    titles.append(title_activities[3].text)
                    print(f"Titulo de la actividad {i + 1} es: ", titles[i])
                    activity_change.append(True)
                    driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Omitir']").click()
                    time.sleep(2)
                else:
                    activity_change.append(False)
            else:
                driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Omitir']").click()
                time.sleep(2)
                find_alert = False
                search_alert = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
                for alert in search_alert:
                    if search_alert[
                        search_alert.index(alert)].text == "No puedes omitir una actividad mas de 3 veces en un dia":
                        find_alert = True
                    else:
                        find_alert = False
                assert find_alert is True, "Error no se mostro la alerta para cuando se ha omitido mas de 3 veces las actividades"
                print("Se mostro correctamente la alerta de omisión de actividades")
                # allure.attach(driver.get_screenshot_as_png(), name="ACT02 Se mostro correctamente la alerta de omision",
                #               attachment_type=AttachmentType.PNG)
                driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'Aceptar']").click()
                break
            assert activity_change[-1] is True, "Error La actividad no cambio al omitirla"
            print(f"La actividad {titles[i]} se omitio correctamente")

    def test_act03(self):

        # Omitir 3 veces una misma actividad. en la cuarta iteracion debera mostrar una
        # alerta indicando que se llego al limite de omisiones por dia, se procedera a
        # ingresar con otro usaurio y corroborar que este usuario pueda omitir
        # sin limitaciones ya que es un usaurio diferente
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestChats)
    unittest.TextTestRunner(verbosity=2).run(suite)
