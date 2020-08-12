from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserDetailsForm
from .models import UserDetails

@login_required
def details(request):

    # Get and pre-fill user-details form
    # see https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
    user_form = UserForm(request.POST, instance=request.user)
    userdetails_form = get_object_or_404(UserDetails, user=request.user.userdetails)

    if request.method == 'GET':
        form = UserDetailsForm(instance=userdetails)
        return render(request, 'userclass/details.html', {'userdetails':userdetails, 'form':form})
    else:
        try:
            form = UserDetails(request.POST, instance=userdetails)
            form.save()
            return redirect('home:home')
        except ValueError:
            return render(request, 'userclass/details.html', {'userdetails':userdetails, 'form':form, 'error':'Bad info'})
