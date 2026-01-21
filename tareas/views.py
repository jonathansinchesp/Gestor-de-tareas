from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Tarea
from .forms import TareaForm

# 1. LISTAR todas las tareas
def lista_tareas(request):
    tareas = Tarea.objects.all().order_by('-fecha_creacion')
    return render(request, 'tareas/lista.html', {'tareas': tareas})

# 2. CREAR nueva tarea
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    
    return render(request, 'tareas/formulario.html', {
        'form': form,
        'titulo_pagina': 'Crear Nueva Tarea'
    })

# 3. EDITAR tarea existente
def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)
    
    return render(request, 'tareas/formulario.html', {
        'form': form,
        'titulo_pagina': f'Editar Tarea: {tarea.titulo}'
    })

# 4. ELIMINAR tarea (con confirmación)
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    
    if request.method == 'POST':
        tarea.delete()
        return redirect('lista_tareas')
    
    return render(request, 'tareas/confirmar_eliminar.html', {
        'tarea': tarea
    })
