import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response


class GetMealByName(APIView):
    def get(self, request):
        _url_to_food_api = "https://themealdb.com/api/json/v1/1/search.php"

        meal_name = request.query_params['meal_name']

        try:
            response_message = requests.get(_url_to_food_api, params={"s": meal_name})
            response_message = response_message.json()
            response_message = response_message["meals"][0]
            print(response_message['idMeal'])
            instruction = response_message['strInstructions']

            ing_counter = 1
            ingredients = {f"Ingredient{ing_counter}": response_message[f'strIngredient{ing_counter}']}

            while response_message[f'strIngredient{ing_counter + 1}']:
                ing_counter += 1
                ingredients[f"Ingredient{ing_counter}"] = response_message[f"strIngredient{ing_counter}"]

            response = {"Meal_Name": meal_name, "Instructions": instruction, "Ingredients": ingredients}
            # print(response)
            return Response(response, content_type=json)
        except():
            return Response("ERROR")


class GetMealsByMainIngredient(APIView):

    def get(self, request):
        _url_to_food_api = "https://themealdb.com/api/json/v1/1/filter.php"

        main_ingredient = request.query_params['ingredient']
        print(f"{main_ingredient}")

        try:
            response_message = requests.get(_url_to_food_api, params={"i": main_ingredient})
            response_message = response_message.json()
            response_message = response_message["meals"]
            meals_counter = 0
            meals_by_category = {f"Meal{meals_counter}": [{"meal_name": response_message[meals_counter]["strMeal"],
                                                           "meal_picture": response_message[meals_counter][
                                                               "strMealThumb"]
                                                           }]}

            while meals_counter < len(response_message):
                i_meal = {"meal_name": response_message[meals_counter]["strMeal"],
                          "meal_picture": response_message[meals_counter]["strMealThumb"]}
                meals_by_category[f"Meal{meals_counter}"] = i_meal
                meals_counter += 1

            return Response(meals_by_category)
        except():
            return Response("ERROR")


class GetMealsByCategory(APIView):

    def get(self, request):
        _url_to_food_api = "https://www.themealdb.com/api/json/v1/1/filter.php"

        category = request.query_params['category']

        try:
            response_message = requests.get(_url_to_food_api, params={"c": category})
            response_message = response_message.json()
            response_message = response_message["meals"]

            meals_counter = 0
            meals_by_category = {f"Meal{meals_counter}": [{"meal_name": response_message[meals_counter]["strMeal"],
                                                           "meal_picture": response_message[meals_counter]["strMealThumb"]
                                                           }]}

            while meals_counter < len(response_message):

                i_meal = {"meal_name": response_message[meals_counter]["strMeal"],
                          "meal_picture": response_message[meals_counter]["strMealThumb"]}
                meals_by_category[f"Meal{meals_counter}"] = i_meal
                meals_counter += 1

            return Response(meals_by_category)
        except():
            return Response("ERROR")


class GetMealsByArea(APIView):

    def get(self, request):
        _url_to_food_api = "https://themealdb.com/api/json/v1/1/filter.php"

        area = request.query_params['area']

        try:
            response_message = requests.get(_url_to_food_api, params={"a": area})
            response_message = response_message.json()
            response_message = response_message["meals"]

            meals_counter = 0
            meals_by_area = {f"Meal{meals_counter}": [{"meal_name": response_message[meals_counter]["strMeal"],
                                                       "meal_picture": response_message[meals_counter][
                                                               "strMealThumb"]
                                                       }]}

            while meals_counter < len(response_message):
                i_meal = {"meal_name": response_message[meals_counter]["strMeal"],
                          "meal_picture": response_message[meals_counter]["strMealThumb"]}
                meals_by_area[f"Meal{meals_counter}"] = i_meal
                meals_counter += 1

            return Response(meals_by_area)
        except():
            return Response("ERROR")
