import requests
from datetime import datetime
# import google

# -------------------------- nutritionix handling ------------------------- #
API_ID = "c1691f39"
API_KEY = "81481143ef48904364c4aca14161a07f"
API_NATURAL_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

HEADERS = {
    "Content-Type": "application/json",
    "x-app-id": "c1691f39",
    "x-app-key": "81481143ef48904364c4aca14161a07f"
}

user_input = input("please write what you did: ")

nutrit_json_api = {
    "query": user_input
}

nutritionix_api = requests.post(url=API_NATURAL_ENDPOINT, headers=HEADERS, json=nutrit_json_api)

nutrit_json_api_get = nutritionix_api.json()

print(nutrit_json_api_get)
# ----------------------------- google sheets handling ----------------------#
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")
posting_json = {
    "sheet1": {
        "date": date,
        "time": time,
        "exercise": nutrit_json_api_get['exercises'][0]['user_input'],
        "duration": nutrit_json_api_get['exercises'][0]['duration_min'],
        "calories": nutrit_json_api_get['exercises'][0]['nf_calories'],
    }
}
print(posting_json)

google_posting = requests.post(url="https://api.sheety.co/005e266bb19297c968f296cd8e26f711/workoutLast/sheet1",
                               json=posting_json)

response = requests.get("https://api.sheety.co/005e266bb19297c968f296cd8e26f711/workoutLast/sheet1")


print(response.text)
