import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row["letter"]: row["code"] for index, row in data.iterrows()}

word = input("Enter a word: ")

final_list = [code_dict[letter.upper()] for letter in word]
print(final_list)
