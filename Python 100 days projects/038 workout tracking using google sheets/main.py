from usefulkeys import appid, appkey
import requests
import json

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    'x-app-id': appid,
    'x-app-key': appkey,
    'x-remote-user-id': '0'
}

exercise_data = {
    'query': input('Tell me which exercises you did: ')
}



response = requests.post(url=exercise_endpoint, headers=headers, data=json.dumps(exercise_data))
print(response.text)
