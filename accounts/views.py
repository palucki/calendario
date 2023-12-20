from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import SignupForm, LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
    
        if form.is_valid():
            user = form.login()
            
            authenticate(username=user.username, password=user.password)

            if user is not None:
                print("authenticated")
                login(request, user)

                return redirect('/dashboard/')
    else: 
        form = LoginForm()

    return render(request, 'accounts/login.html',{
        'form': form
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
    
        if form.is_valid():
            user = form.save()
            
            authenticate(username=user.username, password=user.password)

            if user is not None:
                print("authenticated")
                login(request, user)

                return redirect('/')
            else:
                print("DUPA")
    else: 
        form = SignupForm()

    return render(request, 'accounts/signup.html',{
        'form': form
    })