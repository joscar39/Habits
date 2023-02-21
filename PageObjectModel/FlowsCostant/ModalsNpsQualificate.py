from datetime import datetime, timedelta

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjectModel.action_app.RequestUtils import RequestMethod


class NpsAndRatingStore:
    @staticmethod
    def StatusUserRatingStore(user_id, headers):
        base = None
        url_status = None
        response = None
        res_json = False
        base = RequestMethod.Base_request()
        url_status = f"{base}/api/config/user/userEvaluateStore/{user_id}"
        response = requests.get(url_status, headers=headers)
        res_json = response.json()['data']['callStore']
        return res_json

    @staticmethod
    def DateSurveyNps(email, headers):
        url = None
        response = None
        res_json = None
        base = None
        now = None
        date = None
        result = False
        base = RequestMethod.Base_request()
        url = f"{base}/api/user?where[mail]={email}"
        response = requests.get(url, headers=headers)
        res_json = response.json()['data'][0]['nextSurveyNps'].split(sep="T")[0]
        now = datetime.now().day - 1
        date = datetime.today()+timedelta(days=-int(now))
        if date.strftime('%Y-%m-%d') == res_json:
            result = True
        else:
            result = False
        return result

    @staticmethod
    def ModalsRatingStore(value, driver):
        if value is True:
            skip = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[contains(@text, 'Omitir')]")))
            # Omitir calificacion
            skip.click()
            print("Se Omitio la modal de calificar aplicacion en la tienda")
        else:
            print("no hay modal de calificar en tiendas")

    @staticmethod
    def SkipModalRating(email, headers, driver):
        # Verificar si mostrara modal de calificar aplicacion en tienda
        user_id = RequestMethod.user_id(email, headers)[0]
        status_rating = None
        status_rating = NpsAndRatingStore.StatusUserRatingStore(user_id, headers)
        NpsAndRatingStore.ModalsRatingStore(status_rating, driver)
        