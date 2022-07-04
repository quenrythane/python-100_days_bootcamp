import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = {v["letter"]: v["code"] for k, v in data.iterrows()}
print(data_dict)