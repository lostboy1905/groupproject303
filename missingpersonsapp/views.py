from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request) :
    return render(request, 'missingpersonsapp/index.html')

def BYUPageView(request) :
    return render(request, 'missingpersonsapp/BYU.html')

def contactPageView(request) :
    return render(request, 'missingpersonsapp/contact.html')

def projectsPageView(request) :
    return render(request, 'missingpersonsapp/projects.html')