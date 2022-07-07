import pandas as pd


data = pd.read_csv("day 31 - flash card app/data/french_words.csv")
print(data)
data = data.to_dict()
print(data)

data_dict = {
    "f1": "e1",
    "f2": "e2",
    "f3": "e3",
}

final = {"French": {index: word for index, word in enumerate(data_dict.keys())},
         "English": {index: word for index, word in enumerate(data_dict.values())}}
print(final)
