from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def about(request):
    return render(request, 'home/about.html')

def community(request):
    return render(request, 'home/community.html')

def home(request):
    return render(request, 'home/home.html')

@login_required
def settings(request):
    return render(request, 'home/settings.html')

def testhtml(request):
    return render(request, 'home/testhtml.html')
