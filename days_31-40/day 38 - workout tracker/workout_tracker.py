with open("access_data.txt", "r") as file:
    APP_ID, API_KEY = file.read().split()

print(APP_ID)
print(API_KEY)

