from django.shortcuts import render
from .models import Usuarios,Fila
import csv
import os
from django.conf import settings
from pymongo import MongoClient
import django.core.paginator



# Create your views here.
def usuarios(request):
    usuarios_list=Usuarios.objects.all()
    context = {'lista_usuarios':usuarios_list}
    return render(request,'usuario/usuarios.html',context)

def tabla(request):
    client = MongoClient('localhost', 27017)
    db = client["servicios"]
    collection = db["misservicios"]
    agencias = collection.distinct("agencia")
    mes = collection.distinct("fecha")
    meses = ["01 - Enero","02 - Febrero","03 - Marzo","04 - Abril","05 - Mayo","06 - Junio","07 - Julio","08 - Agosto",
             "09 - Septiembre","10 - Octubre","11 - Noviembre","12 - Diciembre"]
    context = {'agencias': agencias,"meses" : meses}

    if request.method == "POST":
        form = request.POST['agencia']
        form2 = request.POST['mes']
        form3 = request.POST['cantidad']
        form2 = "-"+str(form2).split(" ")[0]+"-"
        print(form2)
        context["filas"]= collection.find({"agencia" : form,'fecha':{"$regex":"^2018"+form2}}).skip(0).limit(int(form3))

        print(form)
    else:
        print("chao")
    return render(request,'usuario/tabla.html',context)