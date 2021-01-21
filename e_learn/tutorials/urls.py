from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.showHome, name="home"),
    path('Videos/',views.videos, name="videos"),
    path('Books/', views.books, name="books"),
    path('Articles/',views.articles,name="articles"),
    path('trial/',views.trial,name="trial"),
    path('search/', views.search, name="search")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)