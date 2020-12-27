import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--fields', action='store', dest='fields', help='all_fields', required=True)

food_search = input("which food category whould u like to search: ")
url = f'https://nutritionix-api.p.rapidapi.com/v1_1/search/{food_search}'
headers = {
    'x-rapidapi-key': "736e99ae1amsh2949ecbc563fbe6p1f85d5jsne4ed66793b05",
    'x-rapidapi-host': "nutritionix-api.p.rapidapi.com"
    }
querystring = {"fields": "item_name,item_id,brand_name,nf_calories,nf_total_fat"}

response = requests.request("GET", url, headers=headers, params=querystring)
response = response.json()
response = response["hits"]
#hits = response[1]["fields"]['item_name']
#hits_test

for x in range(1, 10):
    item_name = response[x]["fields"]['item_name']
    brand_name = response[x]["fields"]["brand_name"]
    calories = response[x]["fields"]["nf_calories"]
    print(f' {x}. item name: {item_name}\n brand name: {brand_name}\n calories: {calories}\n')
else:
    print("the best choices")


#print(f' item name: {item_name}\n brand name: {brand_name}\n calories: {calories}')


#print(response.text)
#hits_test = [1 for response in range(1-10):,]
