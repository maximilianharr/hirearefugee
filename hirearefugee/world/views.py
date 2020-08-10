from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def map(request):
    return render(request, 'world/map.html')

