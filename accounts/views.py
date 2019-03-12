from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['email'])
                return render(request, 'accounts/signup.html', {'error': {
                    'title': 'Email already taken',
                    'message': 'A user with the entered email already exists'
                }})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['email'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
    else:
        return render(request, 'accounts/signup.html')


def login(request, next=None):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            if 'remember_me' in request.POST:
                request.session.set_expiry(1209600) # 2 Weeks
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': {
                    'title': 'Incorrect',
                    'message': 'Username/password is incorrect'
                }})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
