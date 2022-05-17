from django.urls import path
from apps.empleado import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('create', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
