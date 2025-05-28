from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProyectoForm
from django.contrib.auth.decorators import login_required
from .models import Proyecto, Empresa
from .serializers import ProyectoSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

@login_required
def registrar_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.investigador = request.user
            proyecto.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'proyectos/registrar.html', {'form': form})

def lista_proyectos(request):
    proyectos = Proyecto.objects.filter(investigador=request.user)
    return render(request, 'proyectos/lista.html', {'proyectos': proyectos})

def detalle_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    proyectos = Proyecto.objects.filter(empresa=empresa)
    return render(request, 'empresas/detalle_empresa.html', {
        'empresa': empresa,
        'proyectos': proyectos
    })

@login_required
def editar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id, investigador=request.user)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'proyectos/editar.html', {'form': form, 'proyecto': proyecto})

@login_required
def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id, investigador=request.user)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('lista_proyectos')
    return render(request, 'proyectos/eliminar.html', {'proyecto': proyecto})

# SERIALIZERS

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    permission_classes = [AllowAny] 
