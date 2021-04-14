from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def login_page_view(request):
    return render(request, "registration/login.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index_page')
        else:
            messages.info(request, 'Invalid Login Credentials')
            return redirect('login')

    else:
        return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
