from django.contrib import admin
from django.urls import path, include
from .views import home_view, login_view, register_view

urlpatterns = [
    path('', login_view, name='inicio'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('home/', home_view, name='home'),
    

    path("__reload__/", include("django_browser_reload.urls")),
]