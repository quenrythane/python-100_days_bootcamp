import requests as req

params = {
    "amount": 10,
    "category": 17,
    "difficulty": "easy",
    "type": "boolean"
}

question_data = req.get("https://opentdb.com/api.php", params=params).json()['results']
