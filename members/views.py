from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:blog')
        else:
            messages.error(request, ("That is not the valid password or username, please, try again"))
            return redirect('login')
    
    return render(request, 'authentication/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect('blog:blog')
