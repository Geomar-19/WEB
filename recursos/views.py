from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Recurso
# herramientas a la línea donde importas 'render, redirect'
from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, HttpResponseForbidden

def inicio(request):
    todos_los_recursos = Recurso.objects.all().order_by('-fecha_subida')
    return render(request, 'inicio.html', {'recursos': todos_los_recursos})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario) # Inicia sesión automáticamente al registrarse
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')

def descargar_recurso(request, recurso_id):
    # Doble seguridad: verificamos que el usuario haya iniciado sesión
    if not request.user.is_authenticated:
        return redirect('registro')
    
    # Buscamos el recurso en la base de datos
    recurso = get_object_or_404(Recurso, id=recurso_id)
    
    # ¡Sumamos 1 al contador de descargas!
    recurso.descargas += 1
    recurso.save()
    
    # Le enviamos el archivo al usuario para que se descargue
    return FileResponse(recurso.archivo.open(), as_attachment=True)