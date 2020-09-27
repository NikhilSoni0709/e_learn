from django.urls import path
from . import views

urlpatterns = [
    path('',views.showHome, name="home"),
    path('Videos/',views.videos, name="videos"),
    path('Books/', views.books, name="books"),
    path('Articles/',views.articles,name="articles"),
]