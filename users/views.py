from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from .models import Usuario
import json
import re


@csrf_exempt
def register(request):
    if request.method != "POST":
        JsonResponse({"msg": "Solo POST permitido"}, status = 405)
    
    data = json.loads(request.body)
    
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return JsonResponse({"msg": "Falta ingresar USUARIO o CONTRASEÑA"}, status = 400)
    
    if len(password) < 8:
        return JsonResponse({"msg": "La CONTRASEÑA debe tener AL MENOS 8 caracteres"}, status=400)
    if not re.search(r"[A-Z]", password):
        return JsonResponse({"msg": "La CONTRASEÑA debe tener AL MENOS UNA mayuscula"}, status=400)
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return JsonResponse({"msg": "La CONTRASEÑA debe tener AL MENOS UN caracter especial"}, status=400)
    if Usuario.objects.filter(username=username).exists():
        return JsonResponse({"msg": "El USUARIO ingresado ya existe"}, status=400)
    
    
    usuario = Usuario(username=username, password=make_password(password))
    usuario.save()
    
    return JsonResponse({"msg": "Usuario creado"})

@csrf_exempt
def login(request):
    if request.method != "POST":
        return JsonResponse({"msg": "Solo POST permitido"}, status=405)

    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")

    try:
        usuario = Usuario.objects.get(username=username)
    except Usuario.DoesNotExist:
        return JsonResponse({"msg": "Credenciales incorrectas"}, status=401)

    if check_password(password, usuario.password):
        return JsonResponse({"msg": "Inicio de sesión completado"})
    else:
        return JsonResponse({"msg": "Credenciales incorrectas"}, status=401)
