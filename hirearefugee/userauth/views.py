
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'userauth/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            # @todo undo try/except (leave for now due to debugging purposes)
            #try:
            # Add user to DB and login
            user = User.objects.create_user(request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('home')
            #except IntegrityError:
            #    return render(request, 'userauth/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'userauth/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'userauth/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'userauth/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')