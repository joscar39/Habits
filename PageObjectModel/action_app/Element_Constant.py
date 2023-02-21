import time
from selenium.webdriver.common.by import By
from PageObjectModel.action_app.Scroll_util import ScrollUtil


class ElementConstantUtil:

    @staticmethod
    def BackButton(driver):
        # Accion para regresar a la pantalla anterior a traves de la flecha
        # de regresar que se muestra en la pantalla parte superior izquierda
        back_button = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]")
        back_button.click()
        time.sleep(1)

    @staticmethod
    def ModuleChatsBurgerMenu(driver):
        ScrollUtil.open_menu(driver)
        element = None
        element = driver.find_elements(By.XPATH, "//android.widget.TextView")
        elem = 0
        status = False
        for elem in element:
            if element[element.index(elem)].text == "Chats":
                status = True
            else:
                status = False
        assert status is True, "Error, No se muestra la opcion de Chats en el menu hamburguesa"
        driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Chats')]").click()
        time.sleep(1)
