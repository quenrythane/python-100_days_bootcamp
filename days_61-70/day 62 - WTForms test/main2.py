import csv

with open('cafe-data.csv', 'a', newline='', encoding="utf8") as csv_file:
    new_data = ["Mare Street Market","https://goo.gl/maps/ALR8iBiNN6tVfuAA8","8AM","1PM","☕☕","💪💪💪","🔌🔌🔌"]
    writer = csv.writer(csv_file)
    writer.writerow(new_data)


with open('cafe-data.csv', 'r', newline='', encoding="utf8") as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    for row in csv_file:
        print(row)
print(100*"-")