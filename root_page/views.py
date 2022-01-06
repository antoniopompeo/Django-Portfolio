from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects}) #manda como 'projects' la lista de valores que asigne en projects que son todos los objetos que posee a clase Project
