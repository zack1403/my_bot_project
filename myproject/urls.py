from django.contrib import admin
from django.urls import path
from myproject.views import home  # Импортируем нашу функцию

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Главная страница
]