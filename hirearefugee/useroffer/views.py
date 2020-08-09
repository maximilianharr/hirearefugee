
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import UserOfferForm
from .models import UserOffer

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
