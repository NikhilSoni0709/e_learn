from django.urls import path
from . import views

urlpatterns = [
    path('Login/',views.showLoginPage, name="Login"),
    path('Register/',views.showRegisterPage, name="Register"),
    path('logout/', views.showLogoutPage, name="logout")
]