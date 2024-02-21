from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('tg_bot_main/', include('telegram_bot.urls')),
    path('food_services/', include('food_services.urls')),
]
