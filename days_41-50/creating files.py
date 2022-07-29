import os

"""
# creating directory
current_file_path = os.path.dirname(os.path.abspath(__file__))
directory_name = f"day 42 - "
# os.mkdir(directory_name)

# moving file to new directory
file_name = "main2.py"
new_file_path = os.path.join(current_file_path, directory_name, file_name)
print(new_file_path)
"""

for i in range(41, 51):
    directory_name = f"day {i} - "
    os.mkdir(directory_name)
    os.chdir(directory_name)
    with open(f"main.py", "w") as file:
        file.write("print('hello')")
    os.chdir("..")

