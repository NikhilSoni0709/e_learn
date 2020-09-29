from django.shortcuts import render, redirect

# Create your views here.
def showLoginPage(request):
    if(request.method == 'POST'):
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # print(user_name, password)
        return redirect('home')
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
        # print(f_name, user_name, pass_1)
        return redirect('Login')
    else:
        return render(request, 'Register.html')