class AccessData:

    def __init__(self):
        with open("access_data.txt", "r") as file:
            sheety_username, sheety_project_name, sheet_name, bearer_headers = file.read().split()
        self.sheety_username = sheety_username
        self.sheety_project_name = sheety_project_name
        self.sheet_name = sheet_name
        self.bearer_headers = bearer_headers

AD = AccessData()

    