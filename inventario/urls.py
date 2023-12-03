from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),  # Ruta URL base
    path('listar_productos/', views.listar_productos, name='listar_productos'),
    path('productos/', views.listar_productos, name='productos'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('editar_producto/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('inventario/', views.inventario, name='inventario'),

    # ... otras URLs ...
]
