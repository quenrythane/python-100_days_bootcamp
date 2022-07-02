import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")["Primary Fur Color"]
print(data)

# work on data
fur_colors = ["Black", "Cinnamon", "Gray"]
new_data = [len(data[data == "Black"]),
            len(data[data == "Cinnamon"]),
            len(data[data == "Gray"])]
# x = [len(data[data == fur_colors[i]]) for i in range(len(fur_colors))]
print(new_data)

# create final data
data_dict = {
    "Fur Color": fur_colors,
    "Count": new_data
}
print(data_dict)

# save final data to csv
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
