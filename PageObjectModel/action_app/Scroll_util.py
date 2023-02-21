from selenium.webdriver.common.by import By
import time

from PageObjectModel.action_app.Tap_Drag_Util import TapAndDragUtil


class ScrollUtil:

    @staticmethod
    def scroll_to_text(texto, text_constant, driver):
        # Realizar scroll hasta hallar el texto deseado, se debera ingresar el texto deseado y un límite que
        # identifique el último texto visible en pantalla, donde se debra hacer scroll a partir del límite
        # para mostrar el siguiente listado de texto
        scroll_element = None
        found_element = None
        i = 0
        while i < 1:
            time.sleep(1)
            scroll_element = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
            for scroll in scroll_element:
                # print(scroll_element[scroll_element.index(scroll)].text)
                if scroll_element[scroll_element.index(scroll)].text == str(texto):
                    found_element = scroll_element[scroll_element.index(scroll)]
                    print(scroll_element[scroll_element.index(scroll)].text)
                    found_element.click()
                    time.sleep(1)
                    i += 1
                    break
                elif scroll_element[scroll_element.index(scroll)].text == str(text_constant):
                    driver.swipe(263, 1152, 263, 837)
                    time.sleep(1)

    @staticmethod
    def swipe_left_large(howManySwipeToLeft, driver):
        for i in range(1, howManySwipeToLeft + 1):
            driver.swipe(1059, 1164, 63, 1175)
            time.sleep(0.5)

    @staticmethod
    def swipe_right_large(howManySwipeToRight, driver):
        for i in range(1, howManySwipeToRight + 1):
            driver.swipe(39, 1069, 1031, 1048)
            time.sleep(0.5)

    @staticmethod
    def swipe_up_large(howManySwipeToUp, driver):
        for i in range(1, howManySwipeToUp + 1):
            driver.swipe(366, 1302, 375, 389)
            time.sleep(0.5)

    @staticmethod
    def swipe_down_large(howManySwipeToDown, driver):
        for i in range(1, howManySwipeToDown + 1):
            driver.swipe(478, 605, 464, 1463)
            time.sleep(0.5)

    @staticmethod
    def swipe_left_short(howManySwipeToLeft, driver):
        for i in range(1, howManySwipeToLeft + 1):
            driver.swipe(704, 422, 33, 774)
            time.sleep(0.5)

    @staticmethod
    def swipe_right_short(howManySwipeToRight, driver):
        for i in range(1, howManySwipeToRight + 1):
            driver.swipe(202, 896, 537, 884)
            time.sleep(0.5)

    @staticmethod
    def swipe_up_short(howManySwipeToUp, driver):
        for i in range(1, howManySwipeToUp + 1):
            driver.swipe(364, 976, 352, 502)
            time.sleep(0.5)

    @staticmethod
    def swipe_down_short(howManySwipeToDown, driver):
        for i in range(1, howManySwipeToDown + 1):
            driver.swipe(394, 657, 389, 1123)
            time.sleep(0.5)

    @staticmethod
    def swipe_right_short_top(howManySwipeToRight, driver):
        for i in range(1, howManySwipeToRight + 1):
            driver.swipe(202, 570, 551, 565)
            time.sleep(0.5)

    @staticmethod
    def swipe_left_short_top(howManySwipeToLeft, driver):
        for i in range(1, howManySwipeToLeft + 1):
            driver.swipe(596, 570, 216, 570)
            time.sleep(0.5)

    @staticmethod
    def swipe_right_short_low(howManySwipeToRight, driver):
        for i in range(1, howManySwipeToRight + 1):
            driver.swipe(204, 1170, 521, 1166)
            time.sleep(0.5)

    @staticmethod
    def swipe_left_short_low(howManySwipeToLeft, driver):
        for i in range(1, howManySwipeToLeft + 1):
            driver.swipe(530, 1170, 195, 1166)
            time.sleep(0.5)

    @staticmethod
    def swipe_up_into_menu(howManySwipe, driver):
        for i in range(1, howManySwipe + 1):
            driver.swipe(28, 1091, 38, 671)
            time.sleep(0.5)

    @staticmethod
    def swipe_down_into_menu(howManySwipe, driver):
        for i in range(1, howManySwipe + 1):
            driver.swipe(101, 638, 80, 1311)
            time.sleep(0.5)

    @staticmethod
    def scroll_into_menu_to_text(texto, limit, driver):
        scroll_element = None
        i = 0
        while i < 1:
            scroll_element = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
            for scroll in scroll_element:
                # print(scroll_element[scroll_element.index(scroll)].text)
                if scroll_element[scroll_element.index(scroll)].text == str(texto):
                    finded_element_in_menu = scroll_element[scroll_element.index(scroll)]
                    print(scroll_element[scroll_element.index(scroll)].text)
                    finded_element_in_menu.click()
                    time.sleep(2)
                    i += 1
                    break

                elif scroll_element[scroll_element.index(scroll)].text == limit:
                    driver.swipe(28, 1091, 38, 671)
                    time.sleep(1)

    @staticmethod
    def scroll_to_find_text(find_text, constant_text, position_element_break, driver):
        time.sleep(1)
        # find_text: texto que se desea buscar en la pantalla
        # constant_text: Texto que servira de base para que el bucle pueda hacer un scroll y mostrar mas elementos en pantalla
        # position_element_break: Número entero que determina un valor para decir que ya no hay mas elementos para hacer scroll
        i = 0
        find_ele = False
        ele_repe = ["null"]
        while i < 1:
            search_text = None
            search_text = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
            sear = None
            for sear in search_text:
                # print(search_text[search_text.index(sear)].text, "--position--", search_text.index(sear))
                if search_text[search_text.index(sear)].text == f"{find_text} ":
                    find_ele = True
                    time.sleep(1)
                    print("Elemento encontrado")
                    i += 1
                    break
                elif (search_text[search_text.index(sear)].text == str(constant_text)) and (
                        search_text[search_text.index(sear) - int(position_element_break)].text == ele_repe[-1]):
                    find_ele = False
                    i += 1
                    print("No se encontro elemento")
                    break

                elif search_text[search_text.index(sear)].text == str(constant_text):
                    last_position = str(search_text[search_text.index(sear) - int(position_element_break)].text)
                    # print(last_position)
                    ele_repe.append(last_position)
                    driver.swipe(580, 2037, 577, 1843)
                    time.sleep(1)

        return find_ele

    @staticmethod
    def scroll_in_ranking(find_text, constant_text, driver):
        time.sleep(1)
        i = 0
        find_ele = False
        ele_repe = ["null"]
        while i < 1:
            search_text = None
            search_text = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
            sear = None
            for sear in search_text:
                # print(search_text[search_text.index(sear)].text, "--position--", search_text.index(sear))
                if search_text[search_text.index(sear)].text == f"{find_text} ":
                    find_ele = True
                    time.sleep(1)
                    print("Elemento encontrado")
                    i += 1
                    break
                elif (search_text[search_text.index(sear)].text == str(constant_text)) and (
                        search_text[search_text.index(sear) - 4].text == ele_repe[-1]):
                    find_ele = False
                    i += 1
                    print("No se encontro elemento")
                    break

                elif search_text[search_text.index(sear)].text == str(constant_text):
                    last_position = str(search_text[search_text.index(sear) - 4].text)
                    # print(last_position)
                    ele_repe.append(last_position)
                    init_ele = search_text[30]  # Ultimo nombre visible en ranking
                    final_ele = search_text[19]  # Primer nombre visible en ranking
                    TapAndDragUtil.drag_drop_to_element(init_ele, final_ele, driver)
                    # driver.swipe(580, 2037, 577, 1843)
                    time.sleep(1)

        return find_ele

    @staticmethod
    def scroll_to_click_element(find_text, driver):
        time.sleep(1)
        i = 0
        ele_repe = ["null"]
        while i < 1:
            time.sleep(1)
            search_text = None
            search_text = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
            sear = None
            for sear in search_text:
                # print(search_text[search_text.index(sear)].text, "--position--", search_text.index(sear))
                if search_text[search_text.index(sear)].text == f"{find_text}":
                    time.sleep(1)
                    print("Elemento encontrado")
                    search_text[search_text.index(sear)].click()
                    i += 1
                    break
                elif (search_text[search_text.index(sear)].text == "Inicio") and (
                        search_text[search_text.index(sear) - 1].text == ele_repe[-1]):
                    i += 1
                    print("No se encontro elemento")
                    break

                elif search_text[search_text.index(sear)].text == "Inicio":
                    last_position = str(search_text[search_text.index(sear) - 1].text)
                    # print(last_position)
                    ele_repe.append(last_position)
                    ScrollUtil.swipe_up_large(1, driver)
                    # driver.swipe(580, 2037, 577, 1843)
                    time.sleep(1)
            time.sleep(1)

    @staticmethod
    def Scroll_without_limit(find_text, driver):
        time.sleep(1)
        i = 0
        while i < 1:
            search_text = None
            search_text = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
            sear = None
            for sear in search_text:
                # print(search_text[search_text.index(sear)].text, "--position--", search_text.index(sear))
                if search_text[search_text.index(sear)].text == f"{find_text}":

                    time.sleep(1)
                    print("Elemento encontrado")
                    search_text[search_text.index(sear)].click()
                    i += 1
                    break
            ScrollUtil.swipe_up_large(1, driver)
            time.sleep(1)

    @staticmethod
    def open_menu(driver):
        driver.swipe(0, 468, 623, 478)
        time.sleep(1)

    @staticmethod
    def close_notification(driver):
        time.sleep(1)
        driver.swipe(559, 429, 573, 0)
        time.sleep(1)
