from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def index(request):
    return render(request, 'userchat/index.html')

@login_required
def show(request):
    return render(request, 'userchat/show.html')

@login_required
def room(request, room_name):
    return render(request, 'userchat/room.html', {
        'room_name': room_name
    })
