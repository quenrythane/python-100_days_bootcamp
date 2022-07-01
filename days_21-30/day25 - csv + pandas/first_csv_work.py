import csv

with open("weather_data.csv") as file:
    data = list(csv.reader(file))[:-1]

    for line in data:
        print(line)

    temperatures = [int(line[1]) for line in data[1:]]

print(temperatures)
