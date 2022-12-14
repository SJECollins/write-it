from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm

def register(request):
    """
    Register new user.
    Redirects to index.
    """
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
    else:
        form = RegistrationForm()
    context = {'registration_form': form}
    return render(request, 'accounts/register.html', context)


def logout_view(request):
    """
    Logs user out.
    Redirects to index.
    """
    logout(request)
    return redirect('home')


def login_view(request):
    """
    User login.
    Redirects to user profile.
    """
    if request.user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AccountAuthenticationForm()
    context = {'login_form': form}
    return render(request, 'accounts/login.html', context)

