from django.shortcuts import render, redirect
from .models import Usuario
from .forms import RegistroForm, AutenticacionForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from .serializers import UsuarioSerializer
from django.contrib import messages
from rest_framework import viewsets

Usuario = get_user_model()


def home(request):
    return render(request, 'main/home.html')

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.correo_verificado = True
            usuario.save()
            login(request, usuario)

            messages.success(request, 'Usuario creado exitosamente.') 
            return redirect('registro')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def acceder(request):
    form = AutenticacionForm(request.POST or None)

    if request.method =='POST':
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Tu cuenta no está aprobada por el administrador.')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'usuarios/acceder.html', {'form': form})



class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer