import requests
from usefulkeys import token, username

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

requests.post(url=pixela_endpoint, params=user_params)