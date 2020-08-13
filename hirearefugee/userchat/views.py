from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    return render(request, 'userchat/index.html')

def show(request):
    return render(request, 'userchat/show.html')

def room(request, room_name):
    return render(request, 'userchat/room.html', {
        'room_name': room_name
    })
