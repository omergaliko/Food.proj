import requests

url = "https://nutritionix-api.p.rapidapi.com/v1_1/item"

querystring = {"upc":"49000036756"}

headers = {
    'x-rapidapi-key': "736e99ae1amsh2949ecbc563fbe6p1f85d5jsne4ed66793b05",
    'x-rapidapi-host': "nutritionix-api.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)