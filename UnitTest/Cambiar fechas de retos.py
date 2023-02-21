import json
import requests
from datetime import datetime
from datetime import timedelta

base = "https://apiv2desarrollo.habits.ai"
# Obtener token
url = f"{base}/login"
data = {
    "mail": "usuario@habits.ai",
    "pass": "123456789"
}
response = requests.post(url, data=data)
json_response = response.json()
token = json_response['token']
bearer = f'Bearer {token}'
cabecera = {'Content-Type': 'application/json', 'Authorization': f'{bearer}'}
# CAMBIAR FECHAS DE RETOS EN GRUPO E INDIVIDUALES
# Listar retos para la empresa
for i in range(0,
               4):  # rango debe ser limitado por la cantidad de retos que contenga la empresa por tipo individual o grupal
    url2 = f"{base}/api/challenge/?whereObject[company]=620562e673581d0b8417d8e5"
    response2 = requests.get(url2, headers=cabecera)
    json_response2 = response2.json()
    data2 = json_response2['data']
    idchallenge = data2[i]['_id']
    # Modificar fecha de inicio
    url3 = f"{base}/api/challenge/{idchallenge}"
    date = datetime.today()
    new_date = date + timedelta(days=-1)
    dateinit = new_date.strftime('%Y-%m-%d')
    newtime = date.strftime('%H:%M:%S')
    payload = json.dumps({
        "start_date": f"{dateinit}T{newtime}Z"
    })
    response3 = requests.put(url3, headers=cabecera, data=payload)
    # Modificar fecha de finalizacion
    url4 = f"{base}/api/challenge/{idchallenge}"
    date2 = datetime.today()
    timeinit2 = datetime.today()
    new_date2 = date2 + timedelta(days=1)
    dateinit2 = new_date2.strftime('%Y-%m-%d')
    newtime2 = timeinit2.strftime('%H:%M:%S')
    payload2 = json.dumps({
        "end_date": f"{dateinit2}T{newtime2}Z"
    })
    response4 = requests.put(url4, headers=cabecera, data=payload2)
    print(f"proceso del reto {i} terminado")
    print(response4.text)
    print(response4.status_code)

# CAMBIAR FECHAS PARA RETOS PARALELOS


url2 = f"{base}/api/challenge-group?depopulate=true&whereObject[company]=620562e673581d0b8417d8e5"
response2 = requests.get(url2, headers=cabecera)
json_response2 = response2.json()
data2 = json_response2['data']
idchallenge = data2[0]['_id']
print(idchallenge)
# Modificar fecha de inicio
url3 = f"{base}/api/challenge-group/{idchallenge}"
date = datetime.today()
timeinit = datetime.today()
new_date = date + timedelta(days=1)
dateinit = new_date.strftime('%Y-%m-%d')
newtime = timeinit.strftime('%H:%M:%S')
payload = json.dumps({
    "start_date": f"{dateinit}T{newtime}Z"
})
response3 = requests.put(url3, headers=cabecera, data=payload)
print(response3.text)
print(response3.status_code)
# Modificar fecha de finalizacion
url4 = f"{base}/api/challenge-group/{idchallenge}"
date2 = datetime.today()
timeinit2 = datetime.today()
new_date2 = date2 + timedelta(days=1)
dateinit2 = new_date2.strftime('%Y-%m-%d')
newtime2 = timeinit.strftime('%H:%M:%S')
payload2 = json.dumps({
    "end_date": f"{dateinit2}T{newtime2}Z"
})
response4 = requests.put(url4, headers=cabecera, data=payload2)
print("proceso del reto terminado")
print(response4.text)
print(response4.status_code)
