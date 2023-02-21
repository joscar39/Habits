import json
import requests
from datetime import datetime
from datetime import timedelta

base = "https://apiv2desarrollo.habits.ai"
# Obtener token
url_auth = f"{base}/login"
payload_auth = {
    "mail": "lenyn5@habits.ai",
    "pass": "123456789"
}
response_auth = requests.post(url_auth, data=payload_auth)
response_auth_json = response_auth.json()  # Obtener un json de la respuesta
token = response_auth_json['token']  # Hacer un arreglo que guarde el valor de la coincidencia con el texto token
bearer = f'Bearer {token}'
headers = {'Content-Type': 'application/json', 'Authorization': f'{bearer}'}

# Obtener id del usuario
email = "ablades@habits.ai"
url_get_user = f"{base}/api/user/?where[mail]={email}"

response_user_id = requests.get(url_get_user, headers=headers)
rp_user_id_json = response_user_id.json()
data_user = rp_user_id_json['data']
id_user = data_user[0]['_id']
print(id_user)
# Obtener id del habito del usuario

url_id_habits = f"{base}/api/user_habit/?where[user]={id_user}"

rp_id_habit = requests.get(url_id_habits, headers=headers)
rp_id_habit_json = rp_id_habit.json()
data_habits = rp_id_habit_json['data']
data_user_habits = data_habits[0]['habit']
id_habits = data_user_habits['_id']

# Procesar racha diaria

url_racha = f"{base}/api/user/habit/streak/{id_user}"
i = 1
#for i in range(1, 28):
date = datetime.today()
new_date_start = date + timedelta(days=-i)  # valor de i
date_start = new_date_start.strftime('%Y-%m-%d')
newtime = date.strftime('%H:%M:%S')
new_last_score = date + timedelta(days=-1)
date_last_score = new_last_score.strftime('%Y-%m-%d')
payload_racha = json.dumps({
    "streak_start_date": f"{date_start}T{newtime}Z",
    "last_score_date": f"{date_last_score}T{newtime}Z",
    "current_streak": 0,  # valor de i
    "longest_streak": 0,  # valor de i
    "habit": f"{id_habits}"
                      })
response_racha = requests.post(url_racha, headers=headers, data=payload_racha)
print(response_racha.text)
print(response_racha.status_code, f"Se configuro correctamente al usuario {name.value} para inicar racha diaria")