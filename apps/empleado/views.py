from django.shortcuts import render, redirect
from apps.empleado.formmantenimiento import FormMantenimiento
from apps.empleado.models import Mantenimiento
# Create your views here.

def inicio(request):
    mantenimiento = Mantenimiento.objects.all().order_by('id')
    return render(request,'paginas/mantenimiento.html', {'mantenimiento': mantenimiento})

def create(request):
    if request.method == 'POST':
        form = FormMantenimiento(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = FormMantenimiento()
        return render(request,'paginas/mantenimientoform.html', {'form': form})

def update(request,id):
    mantenimiento = Mantenimiento.objects.get(id=id)
    if request.method == 'GET':
        form = FormMantenimiento(instance=mantenimiento)
    else:
        form = FormMantenimiento(request.POST, instance=mantenimiento)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    return render(request, 'paginas/mantenimientoform.html', {'form': form})


def delete(request,id):
    mantenimiento = Mantenimiento.objects.get(id=id)
    mantenimiento.delete()
    return redirect('inicio')