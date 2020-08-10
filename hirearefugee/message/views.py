from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def show(request):
    return render(request, 'message/show.html')
