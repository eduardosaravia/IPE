from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm # Asegúrate de tener un formulario para editar el producto
from .models import Producto
from django.http import JsonResponse

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})


def listar_productos(request):
    productos = Producto.objects.order_by('id')
    categorias = Producto.objects.values('categoria').distinct()
    return render(request, 'listar_productos.html', {'productos': productos, 'categorias': categorias})


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')  # Redirige a la página de lista de productos o a donde desees
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})


def inventario(request):
    return render(request, 'base.html')
