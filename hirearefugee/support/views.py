from django.shortcuts import render

def becomeamember(request):
    return render(request, 'support/becomeamember.html')

def donate(request):
    return render(request, 'support/donate.html')

def helpcoding(request):
    return render(request, 'support/helpcoding.html')

def sponsors(request):
    return render(request, 'support/sponsors.html')

def spreadtheword(request):
    return render(request, 'support/spreadtheword.html')

def thanks(request):
    return render(request, 'support/thanks.html')
