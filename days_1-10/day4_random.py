import random

x = random.randint(1, 10)
print(x, "\n")

a = random.random()
print(a, "\n")

password1 = "abcdef12!@"
password2 = random.shuffle(list(password1))
print(password1, "\n")

"""mix order in string"""
password3 = random.sample(password1, len(password1))
print("".join(password3), "\n")

"""chose 5 random number from 1 to 10"""
password4 = random.sample(range(1, 11), 5)
