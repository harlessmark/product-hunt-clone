from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                # checks if username already taken
                User.objects.get(username=request.POST['username'])
                return render(request, 'account/signup.html', {'error': 'Username already taken'})
            except User.DoesNotExist:
                # creates user
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                # logs in
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'account/signup.html', {'error': 'Passwords don\'t match'})

    else:
        return render(request, 'account/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            # logs in
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/login.html', {'error': 'Username or password is incorrect'})
    else:
        return render(request, 'account/login.html')


def logout(request):
    # make sure this is POST
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'account/logout.html')
