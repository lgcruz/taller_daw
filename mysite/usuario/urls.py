from django.urls import path, include
from . import views

urlpatterns =[
    path(r'',views.usuarios,name='usuarios'),
    path(r'tabla/',views.tabla,name='tabla')
]