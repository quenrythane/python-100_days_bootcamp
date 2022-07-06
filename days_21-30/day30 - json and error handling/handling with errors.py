# FileNotFoundError
"""
with open("not_existing_file.txt", "r") as f:
    print(f.read())
"""

# KeyError
"""
a_dictionary = {"a": 1, "b": 2}
value = a_dictionary["not_existing_key"]
"""

# IndexError
"""
fruit_list = ["apple", "banana", "cherry"]
print(fruit_list[10])
"""

# TypeError
"""
text = "Hello"
print(text + 1)
"""

try:
    with open("not_existing_file.txt", "w") as f:
        print(f.write("Hello"))
    a_dictionary = {"a": 1, "b": 2}
    value = a_dictionary["not_existing_key"]

except FileNotFoundError:
    print("File not found")

except KeyError as error_message:
    print(f"Key {error_message} not found")

else:
    print("Everything is fine (when there is no error)")

finally:
    print("This will always be printed")


# BMI calculator
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
if height > 3:
    raise ValueError("Height is too big")
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.2f}")


