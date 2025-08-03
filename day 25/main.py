import pandas as pd

# with open("weather_data.csv") as wd:
#     f1 = wd.readlines()
#
#     print(f1)
#
#
# import csv
#
# with open("weather_data.csv") as w_d:
#     data = csv.reader(w_d)
#
#     for row in data:
#         print(row)
#
# print("\n\n")
# df = pd.read_csv("weather_data.csv")
# print(df.head())
#
# data_dict = df.to_dict()
# print(data_dict)


df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(df.head())

gray = len(df[df["Primary Fur Color"] == "Gray"])
red = len(df[df["Primary Fur Color"] == "Cinnamon"])
black = len(df[df["Primary Fur Color"] == "Black"])
print(gray,red,black)

data_dict = {
    "Fur Color" : ["gray", "red", "black"],
    "Count":[gray,red,black]
}

pd.DataFrame(data_dict).to_csv("squirrel_count")

