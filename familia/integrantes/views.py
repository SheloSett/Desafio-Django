from django.shortcuts import render
from integrantes.models import Familiares

def new_familar(request):
    new_familiar = Familiares.objects.create(name = "Primo Netu", age = 19 ,description = "Le gusta la jodaa",date_birth = "2002-6-17")
    context = {
        "new_familiar":new_familiar
    }
    return render(request,"new_familiar.html",context=context)

def list_familiar(request):
    familiares = Familiares.objects.all()
    context = {
        "familiares":familiares
    }
    return render(request, "list_familiar.html",context=context)