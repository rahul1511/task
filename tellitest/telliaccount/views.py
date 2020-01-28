from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

# view for registration form

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'your account has been created')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'telliaccount/register.html' , {'form' : form})
        
# views for the profile
@login_required
def profile(request):
    return render(request, 'telliaccount/profile.html')