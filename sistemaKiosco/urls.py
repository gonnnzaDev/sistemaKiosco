from django.contrib import admin
from django.urls import path, include
from .views import login_view, register_view

urlpatterns = [
    path('', login_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),

    path("__reload__/", include("django_browser_reload.urls")),
]