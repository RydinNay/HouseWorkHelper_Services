from django.contrib import admin
from django.urls import path, include
from food_services.views import GetMealByName, GetMealsByMainIngredient, GetMealsByCategory, GetMealsByArea

urlpatterns = [
    path('meals_by_name/', GetMealByName.as_view()),
    path('meals_by_ingredient/', GetMealsByMainIngredient.as_view()),
    path('meals_by_category/', GetMealsByCategory.as_view()),
    path('meals_by_area', GetMealsByArea.as_view()),
]
