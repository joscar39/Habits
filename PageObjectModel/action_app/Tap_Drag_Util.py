import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class TapAndDragUtil:

    @staticmethod
    def tap_screen(x, y, durationMiliSecunds, driver):
        # X: Ubicación en el plano X
        # Y: Ubicación en el plano Y
        # durationMiliSecunds: Colcoar duracion milisegundos el cual durara en hacer click en pantalla
        driver.execute_script('mobile: longClickGesture', {'x': x, 'y': y, 'duration': durationMiliSecunds})

    @staticmethod
    def drag_drop_to_element(initPosition, finalPosition, driver):
        # initPosition : Elemento el cual se desea mover o arrastras
        # finalPosition: Position final a donde se desea mover el elemento, debe ser otro elemento posicionado
        actions = ActionChains(driver)
        actions.drag_and_drop(initPosition, finalPosition)
        actions.perform()

    @staticmethod
    def drag_drop_to_position(element, X, Y, driver):
        actions = ActionChains(driver)
        actions.drag_and_drop_by_offset(element, X, Y)
        actions.perform()

    # Hacer click en boton si encuesta el texto indicado
    @staticmethod
    def search_buttom_contain_text(texto, driver):
        search_buttom = None
        found_buttom = None
        search_buttom = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
        for search in search_buttom:
            if search_buttom[search_buttom.index(search)].text == str(texto):
                found_buttom = search_buttom[search_buttom.index(search)]
                print(search_buttom[search_buttom.index(search)].text)
                found_buttom.click()
                time.sleep(1)
                break
