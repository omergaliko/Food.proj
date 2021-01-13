import requests
import json


def send(key, host, food):
    url = f'https://nutritionix-api.p.rapidapi.com/v1_1/search/{food}'
    headers = {
    'x-rapidapi-key': key,
    'x-rapidapi-host': host
    }
    querystring = {"fields": "item_name,,brand_name,nf_calories,"}


    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    response = response["hits"]

    return response

    # for x in range(1, 3):
    #         item_name = response[x]["fields"]['item_name']
    #         brand_name = response[x]["fields"]["brand_name"]
    #         calories = response[x]["fields"]["nf_calories"]
    #         print(f' {x}. item name: {item_name}\n brand name: {brand_name}\n calories: {calories}\n')
    # else:
    #         print("the best choices")












