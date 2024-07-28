import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)


import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
print(data["temp"].mean())
print(data["temp"].max())

# get data in columns
print(data.condition)

# get data in row
row = data[data.day == "Monday"]
print(row)
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
# print(monday)
monday_temp_F = monday.temp[0] * 9/5 +32
print(f"{monday_temp_F}F")

# Create a dataframe from scratch


data_dict = {
    "students": ["Amy", "Jammy", "Angela"],
    "scores": [20, 40, 48]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")


# working with squirrel dataset

# import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray","Cinnamon", 'Black'],
    "Count":[grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")