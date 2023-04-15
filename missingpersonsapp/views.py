from django.shortcuts import render
from django.http import HttpResponse
from .models import Missing

def indexPageView(request) :
    return render(request, 'missingpersonsapp/index.html')

def BYUPageView(request) :
    return render(request, 'missingpersonsapp/BYU.html')

def contactPageView(request) :
    return render(request, 'missingpersonsapp/contact.html')

def projectsPageView(request) :
    return render(request, 'missingpersonsapp/projects.html')

def addmissingpersonsPageView(request) :
    data = Missing.objects.all()
    context = {"person": data}
    return render(request, 'missingpersonsapp/addmissingpersons.html', context)