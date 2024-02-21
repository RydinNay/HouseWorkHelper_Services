from django.contrib import admin
from django.urls import path, include
from telegram_bot.views import TGBotStart

urlpatterns = [
    path('start/', TGBotStart.as_view())
]
