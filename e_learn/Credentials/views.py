from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def showLoginPage(request):
    if(request.method == 'POST'):
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=user_name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('Login')
    else:
        return render(request, 'Login.html')


def showRegisterPage(request):
    if(request.method == 'POST'):
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        user_name = request.POST['username']
        email = request.POST['email']
        pass_1 = request.POST['password1']
        pass_2 = request.POST['password2']

        if(not User.objects.filter(username=user_name).exists()):
            if(pass_1 != pass_2):
                messages.info(request, "Passwords don't match")
                return redirect('Register')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request, 'Email already registered')
                return redirect('Register')
            else:
                user = User.objects.create_user(first_name=f_name, last_name=l_name, username=user_name, password=pass_1, email=email)
                user.save()
                return redirect('Login')
        else:
            messages.info(request, 'Username Already taken')
            return redirect('Register')
    else:
        return render(request, 'Register.html')


def showLogoutPage(request):
    auth.logout(request)
    return redirect('home')