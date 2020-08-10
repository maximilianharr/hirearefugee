from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def blog(request):
    return render(request, 'blog/blog.html')
