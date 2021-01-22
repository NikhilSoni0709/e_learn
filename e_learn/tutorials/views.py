from django.shortcuts import render, redirect
import json
import requests
from .models import Books, Videos
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def showHome(request):
    return render(request,'home.html')

def videos(request):
    docs = Videos.objects.all()
    # result = Videos.objects.filter(vName='First Video')
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


def search(request):
    if(request.method == 'POST'):
        search = request.POST['search']
        result_books = Books.objects.filter(Q(bTitle__icontains=search) | 
                                    Q(author__icontains=search)  )
        result_videos = Videos.objects.filter(Q(vName__icontains=search))
        
        news_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=9212ff85b9ad4da68751ea8bfaeb8288")

        news = json.loads(news_request.content)

        lst = list(news['articles'])
        result_articles = list()
        for news in lst:
            if(search in news['title']):
                result_articles.append(news)
                continue
            if(search in news['description']):
                result_articles.append(news)

        if not (result_books or result_videos or result_articles):
            messages.info(request, "No result found")
            return redirect('search')
        return render(request,'search.html', { 'searchs_videos': result_videos,'searchs_books': result_books, 'searched':search, 'searchs_articles':result_articles})
    return render(request, 'search.html', )