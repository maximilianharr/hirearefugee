from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import UserOfferForm
from .models import UserOffer
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'useroffer/home.html')

def about(request):
    return render(request, 'useroffer/about.html')

def testhtml(request):
    return render(request, 'useroffer/testhtml.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'useroffer/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentuseroffers')
            except IntegrityError:
                return render(request, 'useroffer/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'useroffer/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'useroffer/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'useroffer/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('currentuseroffers')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def createuseroffer(request):
    if request.method == 'GET':
        return render(request, 'useroffer/createuseroffer.html', {'form':UserOfferForm()})
    else:
        try:
            form = UserOfferForm(request.POST)
            newuseroffer = form.save(commit=False)
            newuseroffer.user = request.user
            newuseroffer.save()
            return redirect('currentuseroffers')
        except ValueError:
            return render(request, 'useroffer/createuseroffer.html', {'form':UserOfferForm(), 'error':'Bad data passed in. Try again.'})

@login_required
def currentuseroffers(request):
    useroffers = UserOffer.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'useroffer/currentuseroffers.html', {'useroffers':useroffers})

@login_required
def completeduseroffers(request):
    useroffers = UserOffer.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'useroffer/completeduseroffers.html', {'useroffers':useroffers})

@login_required
def viewuseroffer(request, useroffer_pk):
    useroffer = get_object_or_404(UserOffer, pk=useroffer_pk, user=request.user)
    if request.method == 'GET':
        form = UserOfferForm(instance=useroffer)
        return render(request, 'useroffer/viewuseroffer.html', {'useroffer':useroffer, 'form':form})
    else:
        try:
            form = UserOfferForm(request.POST, instance=useroffer)
            form.save()
            return redirect('currentuseroffers')
        except ValueError:
            return render(request, 'useroffer/viewuseroffer.html', {'useroffer':useroffer, 'form':form, 'error':'Bad info'})

@login_required
def completeuseroffer(request, useroffer_pk):
    useroffer = get_object_or_404(UserOffer, pk=useroffer_pk, user=request.user)
    if request.method == 'POST':
        useroffer.datecompleted = timezone.now()
        useroffer.save()
        return redirect('currentuseroffers')

@login_required
def deleteuseroffer(request, useroffer_pk):
    useroffer = get_object_or_404(UserOffer, pk=useroffer_pk, user=request.user)
    if request.method == 'POST':
        useroffer.delete()
        return redirect('currentuseroffers')
