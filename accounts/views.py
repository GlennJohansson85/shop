from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth


#___________________________________________________________  DEF REGISTER
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name      = form.cleaned_data['first_name']
            last_name       = form.cleaned_data['last_name']
            email           = form.cleaned_data['email']
            phone_number    = form.cleaned_data['phone_number']
            password        = form.cleaned_data['password']
            username        = email.split("@")[0]
            user = Account.objects.create_user(
                first_name  = first_name,
                last_name   = last_name,
                email       = email,
                password    = password,
                username    = username,
            )
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'Registration Successful!')
            return redirect('register')
    else:
        form = RegistrationForm()
    context  = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


#___________________________________________________________  DEF SIGNIN
def signin(request):
    if request.method == "POST":
        email       = request.POST['email']
        password    = request.POST['password']

        user        = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.signin(request, user)
            # messages.success(request, 'Login Successfull!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('signin')
    return render(request, 'accounts/signin.html')


#___________________________________________________________  DEF SIGNOUT
def signout(request):
    return render