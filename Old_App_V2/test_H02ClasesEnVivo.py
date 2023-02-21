import time
import unittest
import numpy.random
import json
import requests
import openpyxl as xl
import openpyxl
from datetime import datetime
from datetime import timedelta
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjectModel.Global_variables.Path_Data import PathAndVariablesUtil
from TestBase.AppiumSetup import AppSetup
# Ruta de guardado de evidencia
evidence_path = "/"
# Ruta de Base de datos
bd_path = "/"
# Variables de navegacion
chall_nav = "//android.widget.Button[@content-desc=', tab, 5 of 5']/android.view.ViewGroup"


class ClasesEnVivo(unittest.TestCase, AppSetup):
    def setUp(self):
        AppSetup.config(self)

    def test_CLA01(self):  # Entrar a clase en vivo y vincular correo, posteriormente editar el correo vinculado por uno nuevo
        driver = self.driver

        driver.implicitly_wait(20)

        # Activar modo Desarrollo
        for i in range(1, 11):
            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget."
                                          "LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout"
                                          "/android.widget.FrameLayout/android.widget.FrameLayout/android.view."
                                          "ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                                          "android.view.ViewGroup/android.widget.FrameLayout/"
                                          "android.view.ViewGroup/android.view.ViewGroup/android.v"
                                          "iew.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                                          "android.view.ViewGroup/android.view.ViewGroup/android.view."
                                          "ViewGroup[1]/android.widget.ImageView").click()

        modal = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget"
                                              ".LinearLayout/android.widget.FrameLayout/android.widget."
                                              "LinearLayout/android.widget.FrameLayout/android.widget."
                                              "FrameLayout/android.view.ViewGroup/android.view.ViewGroup/"
                                              "android.view.ViewGroup/android.view.ViewGroup/android.widget."
                                              "FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android"
                                              ".view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup"
                                              "/android.view.ViewGroup").is_displayed()
        print("Activado modo desarrollo")
        driver.get_screenshot_as_file(f"{evidence_path}\\recursos\\screenshots\\Retos"
                                      "\\CLA01_ActivadoModoOculto.png")

        # Confirmar si la modal para modo desarrollo esta visible

        if modal is True:
            contra = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget."
                                                   "LinearLayout/android.widget.FrameLayout/android.widget."
                                                   "LinearLayout/android.widget.FrameLayout/android.widget."
                                                   "FrameLayout/android.view.ViewGroup/android.view.ViewGroup"
                                                   "/android.view.ViewGroup/android.view.ViewGroup/android.widget"
                                                   ".FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android"
                                                   ".view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup"
                                                   "/android.view.ViewGroup/android.view.ViewGroup[2]/android."
                                                   "widget.EditText")
            contra.send_keys("12345678")
            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout"
                                          "/android.widget.LinearLayout/android.widget"
                                          ".FrameLayout/android.widget.LinearLayout/android"
                                          ".widget.FrameLayout/android.widget.FrameLayout/android"
                                          ".view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                                          "/android.view.ViewGroup/android.widget.FrameLayout/android.view"
                                          ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android."
                                          "view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                                          "android.view.ViewGroup[3]/android.widget.TextView").click()
        else:
            print("No se desplego la modal")
        time.sleep(2)
        modal2 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/"
                                               "android.widget.LinearLayout/android.widget"
                                               ".FrameLayout/android.widget.LinearLayout/android."
                                               "widget.FrameLayout/android.widget.FrameLayout/android"
                                               ".view.ViewGroup[1]/android.view.ViewGroup/android.view.V"
                                               "iewGroup/android.view.ViewGroup/android.widget.FrameLayout"
                                               "/android.view.ViewGroup/android.view.ViewGroup/android.vi"
                                               "ew.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGr"
                                               "oup/android.view.ViewGroup/android.widget.TextView").is_displayed()

        # Seleccionar opcion Desarrollo
        if modal2 is True:
            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout"
                                          "/android.widget.LinearLayout/android.widget"
                                          ".FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget."
                                          "FrameLayout/android.view.ViewGroup[1]/android"
                                          ".view.ViewGroup/android.view.ViewGroup/android"
                                          ".view.ViewGroup/android.widget.FrameLayout"
                                          "/android.view.ViewGroup/android.view.ViewGroup"
                                          "/android.view.ViewGroup[2]/android.view.ViewGroup"
                                          "/android.view.ViewGroup/android.view.ViewGroup/"
                                          "android.view.ViewGroup[3]/android.view.ViewGroup").click()

            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android."
                                          "widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                          ".LinearLayout/android.widget.FrameLayout/android.widget."
                                          "FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup"
                                          "/android.view.ViewGroup/android.view.ViewGroup/android.widget"
                                          ".FrameLayout/android.view.ViewGroup/android.view.ViewGroup/"
                                          "android.view.ViewGroup[2]/android.view.ViewGroup/android.view"
                                          ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]").click()
            time.sleep(2)
        else:
            print("Modal par seleccionar opcion desarrollo no esta visible")
        driver.get_screenshot_as_file(f"{evidence_path}\\recursos\\screenshots\\Retos"
                                      "\\CLA01_ActivadoModoDesarrollo.png")

        time.sleep(0.5)

        # Iniciar Sesion

        login = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget."
                                              "LinearLayout/android.widget.FrameLayout/android.widget."
                                              "LinearLayout/android.widget.FrameLayout/android.widget."
                                              "FrameLayout/android.view.ViewGroup/android.view.ViewGroup"
                                              "/android.view.ViewGroup/android.view.ViewGroup/android.widget"
                                              ".FrameLayout/android.view.ViewGroup/android.view.ViewGroup"
                                              "/android.view.ViewGroup/android.view.ViewGroup/android.view"
                                              ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                                              "/android.view.ViewGroup[2]")
        login.click()

        filesheet = f"{bd_path}/recursos/ClasesEnVivo.xlsx"
        wb = openpyxl.load_workbook(filesheet)
        datos = wb["Hoja1"]
        email = datos['B1']
        passw = datos['C1']

        mail = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayou"
                                             "t/android.widget.FrameLayout/android.widget.LinearLayout/android."
                                             "widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGrou"
                                             "p/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                                             "/android.widget.FrameLayout/android.view.ViewGroup/android.view.V"
                                             "iewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view"
                                             ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android."
                                             "view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup"
                                             "/android.view.ViewGroup[1]/android.widget.EditText")
        mail.send_keys(email.value)
        driver.hide_keyboard()
        time.sleep(1)

        password = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget."
                                                 "LinearLayout/android.widget.FrameLayout/android.widget."
                                                 "LinearLayout/android.widget.FrameLayout/android.widget.F"
                                                 "rameLayout/android.view.ViewGroup/android.view.ViewGroup"
                                                 "/android.view.ViewGroup/android.view.ViewGroup/android."
                                                 "widget.FrameLayout/android.view.ViewGroup/android.view."
                                                 "ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                                                 "/android.view.ViewGroup/android.view.ViewGroup/android."
                                                 "view.ViewGroup/android.view.ViewGroup[2]/android.widget."
                                                 "ScrollView/android.view.ViewGroup/android.view.ViewGroup"
                                                 "[2]/android.widget.EditText")
        password.send_keys(passw.value)
        driver.get_screenshot_as_file(f"{evidence_path}\\recursos\\screenshots\\Retos"
                                      "\\CLA01_UsuarioCredenciales.png")

        access = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget"
                                               ".LinearLayout/android.widget.FrameLayout/android.widget"
                                               ".LinearLayout/android.widget.FrameLayout/android.widget"
                                               ".FrameLayout/android.view.ViewGroup/android.view.ViewGrou"
                                               "p/android.view.ViewGroup/android.view.ViewGroup/android"
                                               ".widget.FrameLayout/android.view.ViewGroup/android.view"
                                               ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                                               "/android.view.ViewGroup/android.view.ViewGroup/android"
                                               ".view.ViewGroup/android.view.ViewGroup[2]/android.widget"
                                               ".ScrollView/android.view.ViewGroup/android.view.ViewGroup"
                                               "[4]/android.widget.TextView")

        access.click()
        access.click()
        # Alerta de calificacion de aplicacion
        try:
            skip = WebDriverWait(driver, 8). \
                until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[contains(@text, 'Omitir')]")))
            # Omitir calificacion
            skip.click()
            print("Se Omitio la modal de calificar aplicacion en la tienda")
        except:
            print("No hay notificacion de calificacion de aplicacion")

        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                                  ((By.XPATH, PathAndVariablesUtil.challenge_navbar())))
        assert element.is_displayed(), "No se inicio sesion de forma correcta, nos e muestran los elementos del navbar"
        print("Se inicio sesion correctamente")
        # time.sleep(10)
        my_day = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, chall_nav)))

        my_day.click()
        time.sleep(3)
        driver.swipe(460, 1109, 464, 497)

        # Entrar a clase en vivo
        class_in_live = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup")
        class_in_live.click()
        time.sleep(3)
        infografia = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView"
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, str(infografia))))
        no_see_more_info = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[3]")
        no_see_more_info.click()
        buttom_acep_info = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView")
        buttom_acep_info.click()
        time.sleep(2)
        # Modal de vincular cuenta de zoom
        modal_vincular = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView"
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, str(modal_vincular))))
        # Vincular cuenta de zoom y confirmar que se vea en la configuracion
        vincular = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView")
        vincular.click()
        time.sleep(1)
        new_modal_vincular = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, str(new_modal_vincular))))
        send_email_vincular = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText")
        send_email_vincular.send_keys(email.value+"zoom")
        aceptar_vinculacion = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView")
        aceptar_vinculacion.click()
        # Modal de registro exitoso de correo vinculado
        exito = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup"
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, str(exito))))
        driver.get_screenshot_as_file(f"{evidence_path}\\recursos\\screenshots\\Retos"
                                      "\\CLA01_vinculacion exitosa.png")
        close_modal_vinculacion_exitosa = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup")
        close_modal_vinculacion_exitosa.click()
        time.sleep(1)
        # Verificacion si el correo se agrego exitosamente como vinculado del usaurio
        confi_correo_vinculado = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.widget.TextView")
        confi_correo_vinculado.click()
        time.sleep(2)
        correo_vinculado = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[3]").text
        if correo_vinculado == email.value+"zoom":
            print("el correo se vinculo exitosamente")
        else:
            print("Error no es el correo vinculado")
        come_back = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView")
        come_back.click()
        time.sleep(2)
        # Volver a cambiar el correo vinculado
        confi_correo_vinculado.click()
        time.sleep(2)
        edit_mail_vinculado = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[3]")
        edit_mail_vinculado.click()
        email_vincular_new = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText")
        email_vincular_new.send_keys(email.value)
        time.sleep(1)
        aceptar_vinculacion.click()

    def test_CLA02(self):  # Inscribirse a un reto INDIVIDUAL y cumplir con la meta acordada para recibir los puntos indicados
        driver = self.driver

        driver.implicitly_wait(20)

        # Activar modo Desarrollo
        for i in range(1, 11):
            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget."
                                          "LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout"
                                          "/android.widget.FrameLayout/android.widget.FrameLayout/android.view."
                                          "ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                                          "android.view.ViewGroup/android.widget.FrameLayout/"
                                          "android.view.ViewGroup/android.view.ViewGroup/android.v"
                                          "iew.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                                          "android.view.ViewGroup/android.view.ViewGroup/android.view."
                                          "ViewGroup[1]/android.widget.ImageView").click()

        modal = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget"
                                              ".LinearLayout/android.widget.FrameLayout/android.widget."
                                              "LinearLayout/android.widget.FrameLayout/android.widget."
                                              "FrameLayout/android.view.ViewGroup/android.view.ViewGroup/"
                                              "android.view.ViewGroup/android.view.ViewGroup/android.widget."
                                              "FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android"
                                              ".view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup"
                                              "/android.view.ViewGroup").is_displayed()
        print("Activado modo desarrollo")
        driver.get_screenshot_as_file(f"{evidence_path}\\recursos\\screenshots\\Retos"
                                      "\\CLA01_ActivadoModoOculto.png")

        # Confirmar si la modal para modo desarrollo esta visible

        if modal is True:
            contra = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget."
                                                   "LinearLayout/android.widget.FrameLayout/android.widget."
                                                   "LinearLayout/android.widget.FrameLayout/android.widget."
                                                   "FrameLayout/android.view.ViewGroup/android.view.ViewGroup"
                                                   "/android.view.ViewGroup/android.view.ViewGroup/android.widget"
                                                   ".FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android"
                                                   ".view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup"
                                                   "/android.view.ViewGroup/android.view.ViewGroup[2]/android."
                                                   "widget.EditText")
            contra.send_keys("12345678")
            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout"
                                          "/android.widget.LinearLayout/android.widget"
                                          ".FrameLayout/android.widget.LinearLayout/android"
                                          ".widget.FrameLayout/android.widget.FrameLayout/android"
                                          ".view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                                          "/android.view.ViewGroup/android.widget.FrameLayout/android.view"
                                          ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android."
                                          "view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/"
                                          "android.view.ViewGroup[3]/android.widget.TextView").click()
        else:
            print("No se desplego la modal")
        time.sleep(2)
        modal2 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/"
                                               "android.widget.LinearLayout/android.widget"
                                               ".FrameLayout/android.widget.LinearLayout/android."
                                               "widget.FrameLayout/android.widget.FrameLayout/android"
                                               ".view.ViewGroup[1]/android.view.ViewGroup/android.view.V"
                                               "iewGroup/android.view.ViewGroup/android.widget.FrameLayout"
                                               "/android.view.ViewGroup/android.view.ViewGroup/android.vi"
                                               "ew.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGr"
                                               "oup/android.view.ViewGroup/android.widget.TextView").is_displayed()

        # Seleccionar opcion Desarrollo
        if modal2 is True:
            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout"
                                          "/android.widget.LinearLayout/android.widget"
                                          ".FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget."
                                          "FrameLayout/android.view.ViewGroup[1]/android"
                                          ".view.ViewGroup/android.view.ViewGroup/android"
                                          ".view.ViewGroup/android.widget.FrameLayout"
                                          "/android.view.ViewGroup/android.view.ViewGroup"
                                          "/android.view.ViewGroup[2]/android.view.ViewGroup"
                                          "/android.view.ViewGroup/android.view.ViewGroup/"
                                          "android.view.ViewGroup[3]/android.view.ViewGroup").click()

            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android."
                                          "widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                          ".LinearLayout/android.widget.FrameLayout/android.widget."
                                          "FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup"
                                          "/android.view.ViewGroup/android.view.ViewGroup/android.widget"
                                          ".FrameLayout/android.view.ViewGroup/android.view.ViewGroup/"
                                          "android.view.ViewGroup[2]/android.view.ViewGroup/android.view"
                                          ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]").click()
            time.sleep(2)
        else:
            print("Modal par seleccionar opcion desarrollo no esta visible")
        driver.get_screenshot_as_file(f"{evidence_path}\\recursos\\screenshots\\Retos"
                                      "\\CLA01_ActivadoModoDesarrollo.png")

        time.sleep(0.5)

        # Iniciar Sesion

        login = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget."
                                              "LinearLayout/android.widget.FrameLayout/android.widget."
                                              "LinearLayout/android.widget.FrameLayout/android.widget."
                                              "FrameLayout/android.view.ViewGroup/android.view.ViewGroup"
                                              "/android.view.ViewGroup/android.view.ViewGroup/android.widget"
                                              ".FrameLayout/android.view.ViewGroup/android.view.ViewGroup"
                                              "/android.view.ViewGroup/android.view.ViewGroup/android.view"
                                              ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                                              "/android.view.ViewGroup[2]")
        login.click()

        filesheet = f"{bd_path}/recursos/ClasesEnVivo.xlsx"
        wb = openpyxl.load_workbook(filesheet)
        datos = wb["Hoja1"]
        email = datos['B1']
        passw = datos['C1']

        mail = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayou"
                                             "t/android.widget.FrameLayout/android.widget.LinearLayout/android."
                                             "widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGrou"
                                             "p/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                                             "/android.widget.FrameLayout/android.view.ViewGroup/android.view.V"
                                             "iewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view"
                                             ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android."
                                             "view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup"
                                             "/android.view.ViewGroup[1]/android.widget.EditText")
        mail.send_keys(email.value)
        driver.hide_keyboard()
        time.sleep(1)

        password = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget."
                                                 "LinearLayout/android.widget.FrameLayout/android.widget."
                                                 "LinearLayout/android.widget.FrameLayout/android.widget.F"
                                                 "rameLayout/android.view.ViewGroup/android.view.ViewGroup"
                                                 "/android.view.ViewGroup/android.view.ViewGroup/android."
                                                 "widget.FrameLayout/android.view.ViewGroup/android.view."
                                                 "ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                                                 "/android.view.ViewGroup/android.view.ViewGroup/android."
                                                 "view.ViewGroup/android.view.ViewGroup[2]/android.widget."
                                                 "ScrollView/android.view.ViewGroup/android.view.ViewGroup"
                                                 "[2]/android.widget.EditText")
        password.send_keys(passw.value)
        driver.get_screenshot_as_file(f"{evidence_path}\\recursos\\screenshots\\Retos"
                                      "\\CLA01_UsuarioCredenciales.png")

        access = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget"
                                               ".LinearLayout/android.widget.FrameLayout/android.widget"
                                               ".LinearLayout/android.widget.FrameLayout/android.widget"
                                               ".FrameLayout/android.view.ViewGroup/android.view.ViewGrou"
                                               "p/android.view.ViewGroup/android.view.ViewGroup/android"
                                               ".widget.FrameLayout/android.view.ViewGroup/android.view"
                                               ".ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                                               "/android.view.ViewGroup/android.view.ViewGroup/android"
                                               ".view.ViewGroup/android.view.ViewGroup[2]/android.widget"
                                               ".ScrollView/android.view.ViewGroup/android.view.ViewGroup"
                                               "[4]/android.widget.TextView")

        access.click()
        access.click()
        # Alerta de calificacion de aplicacion
        try:
            skip = WebDriverWait(driver, 8). \
                until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[contains(@text, 'Omitir')]")))
            # Omitir calificacion
            skip.click()
            print("Se Omitio la modal de calificar aplicacion en la tienda")
        except:
            print("No hay notificacion de calificacion de aplicacion")

        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                                  ((By.XPATH, PathAndVariablesUtil.challenge_navbar())))
        assert element.is_displayed(), "No se inicio sesion de forma correcta, nos e muestran los elementos del navbar"
        print("Se inicio sesion correctamente")

        # time.sleep(10)
        my_day = WebDriverWait(
            driver, 30).until(EC.presence_of_element_located((By.XPATH, chall_nav)))

        my_day.click()
        time.sleep(3)
        driver.swipe(460, 1109, 464, 497)

        # Entrar a clase en vivo
        class_in_live = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup")
        class_in_live.click()
        time.sleep(3)
        infografia = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView"
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, str(infografia))))
        no_see_more_info = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[3]")
        no_see_more_info.click()
        buttom_acep_info = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView")
        buttom_acep_info.click()
        # Entrar a la clase en vivo
        

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ClasesEnVivo)
    unittest.TextTestRunner(verbosity=2).run(suite)
