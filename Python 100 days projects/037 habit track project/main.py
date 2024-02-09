import requests
from usefulkeys import token, username



# 1. Create an user at pixela API
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}


response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)


# 2. Create a graph definition
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"


graph_params = {
    'id': 'graph1',
    'name': 'Pages Read',
    'unit': 'pages',
    'type': 'int',
    'color': 'momiji'
}


headers = {
    "X-USER-TOKEN": token
}


response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)

# 3. Post value to the graph
pixel_endpoint = f"{graph_endpoint}/{graph_params['id']}"
pixel_params = {
    'date': '20240209', # Don't forget to update everytime you make a post 
    'quantity': '25'
}


response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)