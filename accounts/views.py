from django.shortcuts import render
from .forms import RegistrationForm


def register(request):
    form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def signin(request):
    return render(request, 'accounts/signin.html')


def signout(request):
    return render