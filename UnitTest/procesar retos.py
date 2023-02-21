import time

import requests
base = "https://apiv2desarrollo.habits.ai"
# Obtener token
url_auth = f"{base}/login"
payload_auth = {
    "mail": "lenyn3@habits.ai",
    "pass": "123456789"
}
response_auth = requests.post(url_auth, data=payload_auth)
response_auth_json = response_auth.json()  # Obtener un json de la respuesta
token = response_auth_json['token']  # Hacer un arreglo que guarde el valor de la coincidencia con el texto token
bearer = f'Bearer {token}'
headers = {'Content-Type': 'application/json', 'Authorization': f'{bearer}'}

# Obtener ID de empresa
# url_id_company = f"{base}/api/company/?where[name]=E.C.V Licencias"
url_id_company = f"{base}/api/company/?where[name]=Performance Habits S.A.P.I"
response_id_company = requests.get(url_id_company, headers=headers)
rp_id_comp_json = response_id_company.json()
data_company = rp_id_comp_json['data']
id_company = data_company[0]['_id']

time.sleep(1)

# Listar retos para la empresa

url_challenge = f"{base}/api/challenge/?whereObject[company]={id_company}"
response_challenge = requests.get(url_challenge, headers=headers)
response_auth_challe = response_challenge.json()
data = response_auth_challe['data']
idchallenge = data[3]['_id']
print(idchallenge)
time.sleep(1)

# PROCESAR CRON DE WAITING ROOM
url_waiting_room = f"{base}/api/challenge/processWaitingRoom/{idchallenge}"

response_waiting_room = requests.post(url_waiting_room, headers=headers)
print(response_waiting_room.text)
print(response_waiting_room.status_code)

