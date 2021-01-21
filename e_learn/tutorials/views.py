from django.shortcuts import render
import json
import requests
from .models import Books, Videos

# Create your views here.
def showHome(request):
    return render(request,'home.html')

def videos(request):
    docs = Videos.objects.all()
    return render(request, 'Videos.html', {'docs':docs})

def books(request):
    books = Books.objects.all()
    return render(request, 'Books.html', {'books':books}) 

def articles(request):
    news_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=9212ff85b9ad4da68751ea8bfaeb8288")

    news = json.loads(news_request.content)

    return render(request, 'Articles.html', {'news':news})

def trial(request):
    return render(request, 'trial.html')