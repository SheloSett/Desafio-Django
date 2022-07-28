from django.http import HttpResponse
from django.shortcuts import render


def saludar(request):
    return HttpResponse("Hola Familiaaa, como dice mi amigo Toreto, 'La familia es lo mas importante'")



   