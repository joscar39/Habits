import json
import requests
from datetime import datetime
from datetime import timedelta

from PageObjectModel.action_app.RequestUtils import RequestMethod

email = "joscarlenyn+2@gmail.com"
base = RequestMethod.Base_request()
# Obtener token
headers = None
headers = RequestMethod.header_auth()

# Obtener id del usuario
id_user = RequestMethod.user_id(email, headers)[0]

# # Cambiar ultimo dia de Care
#
# url_habits = f"{base}/api/user/{id_user}"
# date = datetime.today()
# new_date_habits = date + timedelta(days=-130)  # valor de i
# date_habits = new_date_habits.strftime('%Y-%m-%d')
# time_today = date.strftime('%H:%M:%S')
# payload_habit = json.dumps({
#     "last_care": f"{date_habits}T{time_today}Z"
# })

# rp_habit = requests.put(url_habits, headers=headers, data=payload_habit)
# print(rp_habit.text)
# print(rp_habit.status_code)
#
#
# Procesar racha diaria
# RequestMethod.Streak_Daily(id_user, 4, headers)

url_break = None
url_break = f"https://apiv2desarrollo.habits.ai/api/user/habit/streak/{id_user}"

date = datetime.today()
new_date_start = date + timedelta(days=-0)  # valor de i
date_start = new_date_start.strftime('%Y-%m-%d')
newtime = date.strftime('%H:%M:%S')
new_last_score = date + timedelta(days=-1)
date_last_score = new_last_score.strftime('%Y-%m-%d')
payload_racha = json.dumps({
    "streak_start_date": f"{date_start}T{newtime}Z",
    "last_score_date": f"{date_last_score}T{newtime}Z",
    "current_streak": 0,  # valor de i
    "longest_streak": 0,  # valor de i
})
respe_racha = requests.post(url_break, headers=headers, data=payload_racha)
print(respe_racha.status_code)
print(f"request para Actualizar datos de"
      f" racha para el dia 1 fue de status: ", respe_racha.status_code)

# a = ["a","b","o","f","k","h","g"]
# w=0
#
# while w < 1:
#     a = ["a","b","o","f","k","h","g"]
#     for i in a:
#         print(i)
#         if i == "5":
#             print("Finalizado")
#             w += 1
#
#         elif i == "g":
#             a.append(a.index(i))



