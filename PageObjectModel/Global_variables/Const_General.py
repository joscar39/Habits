import time

from selenium.webdriver.common.by import By


class ConstGeneral:
    @staticmethod
    def Courses():
        name_one = None
        name_two = None
        name_one = "Cursos y charlas"
        name_two = "Gym virtual"
        return [name_one, name_two]

    @staticmethod
    def LiveClassRecording():
        one = None
        two = None
        three = None
        one = "Meditación y Yoga"
        two = "Clases grabadas"
        three = "Ejercitate con nosotros"
        return [one, two, three]

    @staticmethod
    def TitleLiveClassRecording():
        a = None
        b = None
        c = None
        d = None
        e = None
        a = "Prueba QA"
        b = "Funcional"
        c = "Power Abs"
        d = "Samurai Fight"
        e = "¡Premiación!"
        return [a, b, c, d, e]

    @staticmethod
    def ScoreDashboard(driver):
        time.sleep(1)
        points = None
        v_point = None
        points = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
        p = None
        for p in points:
            if points[points.index(p)].text == "PUNTOS DEL MES":
                v_point = points[points.index(p) + 1].text
        return v_point


