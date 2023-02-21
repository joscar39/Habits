import json
import requests
from datetime import datetime
from datetime import timedelta

base = "https://apiv2desarrollo.habits.ai"
# base = "https://488d-138-59-8-36.ngrok.io"
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


# OBTENER ID DE USUARIO
email = "permiso@hab.ai"
url_user_id = f"{base}/api/user/?where[mail]={email}"
response_user_id = requests.get(url_user_id, headers=headers)
response_user_id_json = response_user_id.json()
data_user = response_user_id_json['data']
id_user = data_user[0]['_id']
print(id_user)
print(f"Se localizo el usaurio con estatus: {response_user_id.status_code}")
# AJUSTAR DATA D SALUD
cardioid = "5f63a3676070b30de1549bf3"
pasos = "603ededd3522a74b4107ffb4"
sleep = "5f87468222b4c921c00b5286"
id_type_activity = [cardioid, pasos, sleep]
url_data_heal = f"{base}/api/health/addManualData/"
date2 = datetime.today()
dateinit = date2.strftime('%Y-%m-%d')
time_data = date2 + timedelta(minutes=-2)
newtime = time_data.strftime('%H:%M:%S')

payload = json.dumps({
    "date": f"{dateinit} {newtime}",
    "kind": f"{pasos}",
    "timeZone": "America/Caracas",
    "user": f"{id_user}",
    "value": "1600"


    # "date": "2022-04-18 12:37:24",
    # "kind": "603ededd3522a74b4107ffb4",
    # "timeZone": "America/Caracas",
    # "user": "6244b0aab7711fed0372fe65",
    # "value": "8"

          })


response_data_salud = requests.post(url_data_heal, headers=headers, data=payload)
print(response_data_salud.text)
print(f"Se cargo data salud para el usaurio {email} con estatus: {response_data_salud.status_code}")

# ELIMINAR RETO LUEGO DE PRUEBA

# url_delete_challenge = f"{base}/api/challenge/{id_challenge}"

