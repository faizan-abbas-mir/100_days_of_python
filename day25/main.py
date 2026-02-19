"""import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row[1])"""
import pandas

data=pandas.read_csv("weather_data.csv")
print(data["temp"])
"""sum=0
count=0

for temprature in data["temp"]:
    sum=sum+temprature
    count=count+1
average=sum/count
print(average)"""
temp_list=data["temp"].to_list()
print(temp_list)
average2=sum(temp_list)/len(temp_list)
print(average2)
print(data["temp"].mean())
print(data["temp"].max())
print(data.condition)
print(data[data.temp==data.temp.max()])