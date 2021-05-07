from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile = ProfileForm(request.POST)

        if form.is_valid() and profile.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.phone_number = profile.cleaned_data.get('phone_number')
            user.profile.states = profile.cleaned_data.get('states')
            user.profile.cities = profile.cleaned_data.get('cities')
            user.save()
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
        profile = ProfileForm()

    return render(request, 'users/register.html', {'form': form,'profile':profile})

