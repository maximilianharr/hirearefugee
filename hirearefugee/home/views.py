from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def about(request):
    return render(request, 'home/about.html')

def agb(request):
    return render(request, 'home/agb.html')

def cookies(request):
    return render(request, 'home/cookies.html')

def disclaimer(request):
    return render(request, 'home/disclaimer.html')

def community(request):
    return render(request, 'home/community.html')

def home(request):
    return render(request, 'home/home.html') 

def imprint(request):
    return render(request, 'home/imprint.html')

def testhtml(request):
    return render(request, 'home/testhtml.html')
