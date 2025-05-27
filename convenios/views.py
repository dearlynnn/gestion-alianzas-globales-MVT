from django.shortcuts import render, redirect, get_object_or_404
from .models import Empresa, Convenio
from .forms import EmpresaForm, ConvenioForm
from django.contrib.auth.decorators import login_required
from .serializers import EmpresaSerializer, ConvenioSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

@login_required
def lista_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresas/lista_empresas.html', {'empresas': empresas})

@login_required
def crear_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empresas')
    else:
        form = EmpresaForm()
    return render(request, 'empresas/crear_empresa.html', {'form': form})

@login_required
def lista_convenios(request):
    convenios = Convenio.objects.all()
    return render(request, 'convenios/lista_convenios.html', {'convenios': convenios})

@login_required
def crear_convenio(request):
    if request.method == 'POST':
        form = ConvenioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_convenios')
    else:
        form = ConvenioForm()
    return render(request, 'convenios/crear_convenio.html', {'form': form})

# EMPRESAS

@login_required
def editar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    form = EmpresaForm(request.POST or None, instance=empresa)
    if form.is_valid():
        form.save()
        return redirect('lista_empresas')
    return render(request, 'empresas/editar_empresa.html', {'form': form, 'empresa': empresa})

@login_required
def eliminar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    if request.method == 'POST':
        empresa.delete()
        return redirect('lista_empresas')
    return render(request, 'empresas/eliminar_empresa.html', {'empresa': empresa})



# CONVENIOS

@login_required
def editar_convenio(request, convenio_id):
    convenio = get_object_or_404(Convenio, id=convenio_id)
    form = ConvenioForm(request.POST or None, request.FILES or None, instance=convenio)
    if form.is_valid():
        form.save()
        return redirect('lista_convenios')
    return render(request, 'convenios/editar_convenio.html', {'form': form, 'convenio': convenio})

@login_required
def eliminar_convenio(request, convenio_id):
    convenio = get_object_or_404(Convenio, id=convenio_id)
    if request.method == 'POST':
        convenio.delete()
        return redirect('lista_convenios')
    return render(request, 'convenios/eliminar_convenio.html', {'convenio': convenio})

# SERIALIZERS
class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [AllowAny] 

class ConvenioViewSet(viewsets.ModelViewSet):
    queryset = Convenio.objects.all()
    serializer_class = ConvenioSerializer
    permission_classes = [AllowAny] 