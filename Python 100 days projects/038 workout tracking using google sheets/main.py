from usefulkeys import appid, appkey
import requests
import json
from datetime import datetime
# ======================================================================================================
# EXERCICIE API REGISTER
workouts = input('Tell me which exercises you did: ')
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    'x-app-id': appid,
    'x-app-key': appkey,
    'x-remote-user-id': '0'
}

exercise_data = {
    'query': workouts
}



response = requests.post(url=exercise_endpoint, headers=headers, data=json.dumps(exercise_data))
data = response.json()
print(data)

date = f"{datetime.now()}".split()[0]
hour = f"{datetime.now()}".split()[1]
exercise = (data["exercises"][0]['name'])
duration = (data["exercises"][0]['duration_min'])
calories = (data["exercises"][0]['nf_calories'])
# printings to test
print(date)
print(hour)
print(exercise)
print(duration)
print(calories)
# ======================================================================================================
# SHEETY API
from usefulkeys import username, projectName, sheetName

# GET REQUEST
sheety_endpoint = f'https://api.sheety.co/{username}/{projectName}/{sheetName}'
sheety_params = {
    'username': username,
    'projectName': projectName,
    'sheetName': sheetName
}

response2 = requests.get(url=f'https://api.sheety.co/{username}/{projectName}/{sheetName}')
print(response2.text)

# Add a row
# To create a new row in your sheet, perform a POST request to the endpoint, with your row contents as a JSON payload in the request body.

# Sheety expects your record to be nested in a singular root property named after your sheet. For example if your endpoint is named emails, 
# nest your record in a property called email.
# POST REQUEST
from usefulkeys import userid, email
headers = {
    "Content-Type": "application/json",
    # Se a sua API Sheety requer autenticação, descomente e ajuste a linha abaixo
    # "Authorization": "Bearer SEU_TOKEN_DE_ACESSO"
}

data = {
    'workouts': [
        {
            'date': date,
            'time': hour,
            'exercise': exercise,
            'duration': duration,
            'calories': calories
        }
    ]
} 

response3 = requests.post(url=sheety_endpoint, json=data, headers=headers)

print(response3.text)
print(response3)