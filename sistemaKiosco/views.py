from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def login_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'login.html')

def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')

def register_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'register.html')

