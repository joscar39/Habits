import json
import requests
from datetime import datetime
from datetime import timedelta


class RequestMethod:

    @staticmethod
    def Base_request():
        base = None
        base = "https://apiv2desarrollo.habits.ai"
        return base

    @staticmethod
    def header_auth(email="request@habitsqa.com", password="Aa123456."):
        base = None
        base = RequestMethod.Base_request()
        url_auth = f"{base}/login"
        payload_auth = {
            "mail": email,
            "pass": password
        }
        response_auth = None
        response_auth = requests.post(url_auth, data=payload_auth)
        response_auth_json = None
        response_auth_json = response_auth.json()  # Obtener un json de la respuesta
        token = None
        token = response_auth_json['token']  # Hacer un arreglo que guarde el valor del texto token
        bearer = None
        bearer = f'Bearer {token}'
        header = None
        headers = {'Content-Type': 'application/json', 'Authorization': f'{bearer}'}

        return headers

    @staticmethod
    def user_id(email, headers_rq):
        base = RequestMethod.Base_request()
        url_get_user = f"{base}/api/user/?where[mail]={email}"
        response_user_id = requests.get(url_get_user, headers=headers_rq)
        rp_user_id_json = response_user_id.json()
        data_user = rp_user_id_json['data']
        id_user = data_user[0]['_id']
        name_user = data_user[0]['name']
        company_user = data_user[0]['company']['_id']

        return [id_user, name_user, company_user]

    @staticmethod
    def point_user(points, name_user, id_user, headers_rq):
        base = None
        base = RequestMethod.Base_request()
        url_point_user = f"{base}/api/points/user/multiple"
        date = None
        date = datetime.today()
        today_is = None
        today_is = date.strftime('%Y-%m-%d')
        time = None
        time = date.strftime('%H:%M:%S')
        payload_point_user = json.dumps([
            {
                "title": f"Puntos de ranking",
                "description": f"puntos para usuario {name_user}",
                "points": points,
                "users": f"{id_user}",
                "categoryKey": 4,
                "date": f"{today_is}T{time}-00:00"
            }
        ])
        response_point_user = None
        response_point_user = requests.post(url_point_user, headers=headers_rq, data=payload_point_user)
        print("Request for add point at user is: ", response_point_user.status_code)

    @staticmethod
    def masive_point_users(name_user_one, points_one, id_user_one, name_user_two, points_two,
                           id_user_two, name_user_three, points_three, id_user_three,
                           name_user_four, points_four, id_user_four, headers_rq):
        base_url = None
        base_url = RequestMethod.Base_request()
        url_point_user = f"{base_url}/api/points/user/multiple"
        date = None
        date = datetime.today()
        today_is = None
        today_is = date.strftime('%Y-%m-%d')
        time = None
        time = date.strftime('%H:%M:%S')
        payload_masive_point = json.dumps([
            {
                "title": f"Puntos de ranking",
                "description": f"puntos para usuario {name_user_one}",
                "points": points_one,
                "users": f"{id_user_one}",
                "categoryKey": 4,
                "date": f"{today_is}T{time}-00:00"
            },
            {
                "title": f"Puntos de ranking",
                "description": f"puntos para usuario {name_user_two}",
                "points": points_two,
                "users": f"{id_user_two}",
                "categoryKey": 4,
                "date": f"{today_is}T{time}-00:00"
            },
            {
                "title": f"Puntos de ranking",
                "description": f"puntos para usuario {name_user_three}",
                "points": points_three,
                "users": f"{id_user_three}",
                "categoryKey": 4,
                "date": f"{today_is}T{time}-00:00"
            },
            {
                "title": f"Puntos de ranking",
                "description": f"puntos para usuario {name_user_four}",
                "points": points_four,
                "users": f"{id_user_four}",
                "categoryKey": 4,
                "date": f"{today_is}T{time}-00:00"
            }
        ])
        response_point_masive = None
        response_point_masive = requests.post(url_point_user, headers=headers_rq, data=payload_masive_point)
        print("Request of add point masive is: ", response_point_masive.status_code)

    @staticmethod
    def delete_point_by_company(id_company, headers_rq):
        base = None
        base = RequestMethod.Base_request()
        url_delete_point_by_company = None
        url_delete_point_by_company = f"{base}/api/user_points_months/ranking/company/{id_company}"
        request_delete_point = requests.delete(url_delete_point_by_company, headers=headers_rq)
        print("Request of delete point is: ", request_delete_point.status_code)

    @staticmethod
    def Get_habit_user(id_user, headers):
        url_id_habits = None
        base_url = None
        base_url = RequestMethod.Base_request()
        url_id_habits = f"{base_url}/api/user_habit/?where[user]={id_user}"

        rp_id_habit = requests.get(url_id_habits, headers=headers)
        rp_id_habit_json = rp_id_habit.json()
        data_habits = rp_id_habit_json['data']
        data_user_habits = data_habits[0]['habit']
        id_habits = data_user_habits['_id']
        return id_habits

    @staticmethod
    def Get_id_UserLogPoint(id_user, headers):
        url_logpoint = None
        base_url = None
        base_url = RequestMethod.Base_request()
        url_logpoint = f"{base_url}/api/medal_for_points/user/{id_user}/?historyPoints=true&page=0&limit=5"

        response_logpoint = requests.get(url_logpoint, headers=headers)
        rp_logpoint_json = response_logpoint.json()
        data_logpoint = rp_logpoint_json['data']
        data_point = data_logpoint['logPoints']
        id_lpoint = data_point[0]['_id']
        return id_lpoint

    @staticmethod
    def Put_description_of_point(day, id_logpoint, headers):
        url_description = None
        base_url = None
        base_url = RequestMethod.Base_request()
        url_description = f"{base_url}/api/points/user/{id_logpoint}"
        payload_description = json.dumps({
            "description": f"Recompensa por cumplir tu hábito del dia {day}"  # Descripcion modificada
        })
        response_description = requests.put(url_description, headers=headers, data=payload_description)
        print(response_description.status_code, f"Descripción modificada exitosamente, para el dia {day}")

    @staticmethod
    def Streak_Daily(id_user, value_of_days, headers):
        url_racha = None
        base_url = None
        base_url = RequestMethod.Base_request()
        url_racha = f"{base_url}/api/user/habit/streak/{id_user}"

        date = datetime.today()
        new_date_start = date + timedelta(days=-value_of_days)  # valor de i
        date_start = new_date_start.strftime('%Y-%m-%d')
        newtime = date.strftime('%H:%M:%S')
        new_last_score = date + timedelta(days=-1)
        date_last_score = new_last_score.strftime('%Y-%m-%d')
        payload_racha = json.dumps({
            "streak_start_date": f"{date_start}T{newtime}Z",
            "last_score_date": f"{date_last_score}T{newtime}Z",
            "current_streak": value_of_days,  # valor de i
            "longest_streak": value_of_days  # valor de i
        })
        respe_racha = requests.post(url_racha, headers=headers, data=payload_racha)
        print(f"request para Actualizar datos de"
              f" racha para el dia {value_of_days} fue de status: ", respe_racha.status_code)

    @staticmethod
    def Break_streak(id_user, value_of_days, longest_streak, headers):
        url_break = None
        base_url = None
        base_url = RequestMethod.Base_request()
        url_break = f"{base_url}/api/user/habit/streak/{id_user}"
        date = None
        new_date_start = None
        newtime = None
        date_last_score = None
        date = datetime.today()
        new_date_start = date + timedelta(days=-value_of_days)  # valor de i
        date_start = new_date_start.strftime('%Y-%m-%d')
        newtime = date.strftime('%H:%M:%S')
        new_last_score = date + timedelta(days=-value_of_days)
        date_last_score = new_last_score.strftime('%Y-%m-%d')
        payload_racha = json.dumps({
            "streak_start_date": f"{date_start}T{newtime}Z",
            "last_score_date": f"{date_last_score}T{newtime}Z",
            "longest_streak": longest_streak  # valor de i
        })
        respe_racha = requests.post(url_break, headers=headers, data=payload_racha)
        print(f"request para romper la racha diaria fue de status: ", respe_racha.status_code)

