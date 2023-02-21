import json

import requests

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
email = "pie@habits.ai"
url_get_user = f"{base}/api/user/?where[mail]={email}"

response_user_id = requests.get(url_get_user, headers=headers)
rp_user_id_json = response_user_id.json()
data_user = rp_user_id_json['data']
id_user = data_user[0]['_id']

url_logpoint = f"https://apiv2desarrollo.habits.ai/api/medal_for_points/user/{id_user}/?historyPoints=true&page=0&limit=5"

response_logpoint = requests.get(url_logpoint, headers=headers)
rp_logpoint_json = response_logpoint.json()
data_logpoint = rp_logpoint_json['data']
data_point = data_logpoint['logPoints']
id_logpoint = data_point[0]['_id']

# Cambiar datos del description
url_description = f"https://apiv2desarrollo.habits.ai/api/points/user/{id_logpoint}"
i = 1
payload_description = json.dumps({
    "description": f"Recompensa por cumplir tu hábito del dia {i}"  # Descripcion modificada
})

response_description = requests.put(url_description, headers=headers, data=payload_description)
print(response_description.status_code, f"Descripcion modificada exitosamente para el dia {i}")
