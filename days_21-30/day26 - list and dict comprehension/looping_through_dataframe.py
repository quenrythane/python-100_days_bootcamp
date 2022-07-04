import pandas as pd

students_dict ={
    "names": ["Arthur", "Ben", "Chris"],
    "score": [50, 66, 75]
}

students_df = pd.DataFrame(students_dict)

print(students_dict)
print(students_df)
print("-"*100)


for k, v in students_df.items():
    print(k)
print("-"*100)

for k, v in students_df.items():
    print(v)
print("-"*100)

# loop through rows of df
for index, row in students_df.iterrows():
    print(index)
print("-"*100)

for index, row in students_df.iterrows():
    print(row)
print("-"*100)

for index, row in students_df.iterrows():
    print(row.names, row.score)
print("-"*100)

