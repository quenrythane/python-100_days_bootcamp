import os

def check_catalogs_numbers():

    current_path = os.path.dirname(os.path.abspath(__file__))
    numbers = [int(num) for num in current_path[current_path.find("\days_") + 6:].split("-")]
    return numbers

def create_catalogs_with_file(numbers):
    for i in range(numbers[0], numbers[1] + 1):
        directory_name = f"day {i} - "
        os.mkdir(directory_name)
        os.chdir(directory_name)
        with open(f"main.py", "w") as file:
            file.write("print('hello')")
        os.chdir("..")

create_catalogs_with_file(check_catalogs_numbers())
