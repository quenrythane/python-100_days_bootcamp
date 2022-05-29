def tak(x):
    if x == 10:
        print("?")
        return 15
    else:
        print(x)
        tak(x + 1)

print(tak(5))
