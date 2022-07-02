import csv
import pandas

with open("weather_data.csv") as file:
    data = list(csv.reader(file))[:-1]

    # display data
    for line in data:
        print(line)

    # exercise from lecture
    temperatures = [int(line[1]) for line in data[1:]]
    print(temperatures, "\n"*2)


"""Pandas"""
data = pandas.read_csv("weather_data.csv")
# DataFrame
print(data, "\n")


# series (alone column - something aka list)
print(data["temp"])
temp_list = data["temp"].to_list()
print(temp_list)
print(data["temp"].mean(), "\n")


print(data["condition"])
print(data.condition, "\n")


data_dict = data.to_dict()
print(data_dict, "\n")


# get data in row
print(data[data["day"] == "Monday"])
# we could filter by condition
print(data[data["temp"] == data["temp"].max()])
print(data["temp"] == data["temp"].max())


# Create DataFrame
data_dict = {
    "students": ["Arthur", "Baltazar", "Charming"],
    "score": [50, 66, 92],
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("pandas_csv/new_data.csv")
