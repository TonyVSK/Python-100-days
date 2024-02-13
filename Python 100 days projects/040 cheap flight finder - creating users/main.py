from usefulkeys import username, projectName, sheetName, authorization
import requests



# # GET INFORMATION
# sheety_endpoint = f'https://api.sheety.co/{username}/{projectName}/{sheetName}'
# sheety_params = {
#     'username': username,
#     'projectName': projectName,
#     'sheetName': sheetName
# }
# response = requests.get(url=f'https://api.sheety.co/{username}/{projectName}/{sheetName}')
# print(response.text)
# print(response.status_code)

# POST USER INFORMATION

print('Welcome to the flight clube')
name= input('Please insert your first name: ')
lastName = input('Insert your last name: ')
email1 = 0
email2 = 1
while email1 != email2:
    email1 = input('Insert your email: ')
    email2 = input('Repeat again your email: ')
    if email1 != email2:
        print("The email don't match; please try again")

sheety_endpoint = f'https://api.sheety.co/{username}/{projectName}/{sheetName}'
sheety_params = {
    'username': username,
    'projectName': projectName,
    'sheetName': sheetName
}



headers = {
    "Authorization": f"Bearer {authorization}"
}

users = {
    'user': 
        {
            'name': name,
            'lastName': lastName,
            'email': email1
        }
    
} 



response = requests.post(url=f'https://api.sheety.co/{username}/{projectName}/{sheetName}', json=users, headers=headers)
print(response.text)
print(response.status_code)