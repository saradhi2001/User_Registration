from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
    
            user = authenticate(username=user.username, password=password)
            if user is not None:
                login(request, user)
            return redirect('home')  # Redirect to home page after registration
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})