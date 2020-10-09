from django.shortcuts import render

# Create your views here.

def showHome(request):
    return render(request,'home.html')

def videos(request):
    return render(request, 'Videos.html')

def books(request):
    return render(request, 'Books.html') 

def articles(request):
    return render(request, 'Articles.html')

def trial(request):
    return render(request, 'trial.html')