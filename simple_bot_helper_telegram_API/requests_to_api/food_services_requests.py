import os
from dotenv import load_dotenv

import requests
import json

load_dotenv()

main_url = os.getenv('requests_main_url')


def get_meal_recipe(meal_name):
    headers = {'Content-Type': 'application/json'}

    response = requests.get(main_url + "food_services/meals_by_name", params={'meal_name': meal_name}, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.content)
        
        answer = f"Here is instruction for {data['Meal_Name']}:\r\n" \
                 f"{data['Instructions']}.\r\n"\
                 f"This is all ingredients that you need:\r\n"\
                 f"{data['Ingredients']}"
        return answer
    return None


def get_meals_by_main_ingredient(ingredient):
    headers = ""

    response = requests.get(main_url + "food_services/meals_by_ingredient", params={'ingredient': ingredient}, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.content)

        return data
    return None


def get_meals_by_category(category):
    headers = ""
    response = requests.get(main_url + "food_services/meals_by_category", params={'category': category})

    if response.status_code == 200:
        data = json.loads(response.content)

        return data
    return None


def get_meals_by_area(category):
    headers = ""
    response = requests.get(main_url + "food_services/meals_by_area", params={'area': category})

    if response.status_code == 200:
        data = json.loads(response.content)

        return data
    return None
