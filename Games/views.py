from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from .models import Game

def index(request):
    games =  Game.objects.all()
    return render(request,'/Users/coder/Desktop/Django_file/Games/templates/index.html',
                  {'games':games})

def new(request):
    #return render(request, 'new.html')
    return HttpResponse('Hello world')
