# with open('weather_data.csv', 'r') as file:
#     data = file.readlines()
#     print(data)

# import csv


# with open('weather_data.csv', 'r') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for eachData in data:
#         if eachData[1] != 'temp':
#             temperatures.append(int(eachData[1]))
    

# print(temperatures)



import pandas as pd
data = pd.read_csv("weather_data.csv")
print(data)
print(data['temp'])