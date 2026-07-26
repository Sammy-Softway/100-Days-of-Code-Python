# with open("weather_data.csv","r") as weather_data_file:
#     weather_data = weather_data_file.readlines()
#     print(weather_data)

# import csv
# with open("weather_data.csv") as weather_file:
#     weather_file = csv.reader(weather_file)
#
#     temperatures = []
#
#     for row in weather_file:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# # data_list = data["temp"].to_list()
# data_list = data.temp.to_list()     #same as initial line above
#
# print(data_list)
# print(len(data_list))
#
# average_temp = sum(data_list) / len(data_list)
# print(average_temp)
#
# #learn functions from the panda documentation
# print(data["temp"].mean())
# print(data.temp.mean())   #same as initial line above
#
# print(data["temp"].max())
# print(data.temp.max)  #same as the initial line above


#Get data in a row
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp)
#
# monday_temp_celsius = monday.temp[0]
# monday_temp_fahrenheit = (monday_temp_celsius * 1.8) + 32
# print(monday_temp_fahrenheit)


#Create a DataFrame from scratch
# data_dict ={
#     "students": ["Samuel", "Michael", "Daniel"],
#     "Scores": [91, 92, 93]
# }
#
# new_data = pandas.DataFrame(data_dict)
# # print(new_data)
# new_data.to_csv("new_data.csv")


squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_color_list = squirrel_data["Primary Fur Color"].to_list()
# print(squirrel_color_list)
# print(len(squirrel_color_list))

gray_squirrel = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
black_squirrel = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]
cinnamon_squirrel = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]

gray_squirrel_count = len(gray_squirrel)
black_squirrel_count = len(black_squirrel)
cinnamon_squirrel_count = len(cinnamon_squirrel)


squirrel_color_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrel_count, black_squirrel_count, cinnamon_squirrel_count],
}

squirrel_color_frame = pandas.DataFrame(squirrel_color_dict)
print(squirrel_color_frame)
squirrel_color_frame.to_csv("squirrel_color_counts.csv")