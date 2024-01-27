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



# import pandas as pd
# data = pd.read_csv("weather_data.csv")



# Create data in a row
# print(data[data.temp == maxTemp])
# print(data[data.temp == data.temp.max()])


# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data=pd.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import pandas as pd

counter=0

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
new_grey_squirrels=len(grey_squirrels)
print(new_grey_squirrels)

red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
new_red_squirrels=len(red_squirrels)
print(new_red_squirrels)

black_squirrels = data[data["Primary Fur Color"] == "Black"]
new_black_squirrels=len(black_squirrels)
print(new_black_squirrels)

data_dict = {
    "Squirrel Colors": ["Grey", "Red", "Black"],
    "Numbers": [new_grey_squirrels, new_red_squirrels, new_black_squirrels]
}

data_dict=pd.DataFrame(data_dict)
data_dict.to_csv("squirrelCounter.csv")