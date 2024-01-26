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



# Create data in a row
# print(data[data.temp == maxTemp])
# print(data[data.temp == data.temp.max()])


# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data=pd.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")