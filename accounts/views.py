#_________________________________________________________________________  ACCOUNTS/VIEWS.PY
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, UserForm, UserProfileForm
from .models import Account, UserProfile
from orders.models import Order
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


#___________________________________________________________  VERIFICATION EMAIL
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

from cart.views import _cart_id
from cart.models import Cart, CartItem

import requests

#___________________________________________________________  DEF REGISTER
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name          = form.cleaned_data['first_name']
            last_name           = form.cleaned_data['last_name']
            phone_number        = form.cleaned_data['phone_number']
            email               = form.cleaned_data['email']
            password            = form.cleaned_data['password']
            username            = email.split("@")[0]
            user                = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number   = phone_number
            user.save()

            # USER ACTIVATION
            current_site        = get_current_site(request)
            mail_subject        = 'Please activate your account'
            message             = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email            = email
            send_email          = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(request, 'Activation link sent to your email!')
            return redirect('/accounts/signin/?command=verification&email='+email)
    else:
        form                    = RegistrationForm()
    context                     = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)



#___________________________________________________________  DEF SIGNIN
def signin(request):
    if request.method           == "POST":
        email                   = request.POST['email']
        password                = request.POST['password']
        user                    = auth.authenticate(email=email, password=password)

        if user is not None:
            try:
                cart            = Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    cart_item   = CartItem.objects.filter(cart=cart)

                    # GET product variation by cart id
                    product_variation = []
                    for item in cart_item:
                        variation = item.variations.all()
                        product_variation.append(list(variation))

                    # GET cart items from user - access products variations
                    cart_item   = CartItem.objects.filter(user=user)
                    ex_var_list = []
                    id          = []
                    for item in cart_item:
                        existing_variation = item.variations.all()
                        ex_var_list.append(list(existing_variation))
                        id.append(item.id)    

                    # product_variation = [1,2,3,4,6]
                    # ex_var_list =[4,6,3,5]

                    for pr in product_variation:
                        if pr in ex_var_list:
                            index           = ex_var_list.index(pr)
                            item_id         = id[index]
                            item            = CartItem.objects.get(id=item_id)
                            item.quantity   += 1
                            item.user       = user
                            item.save()
                        else:
                            cart_item       = CartItem.objects.filter(cart=cart)
                            for item in cart_item:
                                item.user   = user
                                item.save()
            except:
                pass
            auth.login(request, user)
            messages.success(request, 'Login Successfull!')
            url = request.META.get('HTTP_REFERER')
            try:
                query = requests.utils.urlparse(url).query
                params = dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage = params['next']
                    return redirect('nextPage')
            except:
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Login Credentials.')
            return redirect('signin')
    return render(request, 'accounts/signin.html')


#___________________________________________________________  DEF SIGNOUT
@login_required(login_url = 'signin')
def signout(request):
    auth.logout(request)
    messages.success(request, 'Loggout Successful!')
    return redirect('signin')


#___________________________________________________________  DEF ACTIVATE
def activate(request, uidb64, token):
    try:
        uid     = urlsafe_base64_decode(uidb64).decode()
        user    = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user    = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account is activated!')
        return redirect('signin')
    else:
        messages.error(request, 'invalid activation link')
    return redirect('register')


#___________________________________________________________  DEF DASHBOARD
@login_required(login_url = 'signin')
def dashboard(request):
    orders = Order.objects.order_by('-created_at').filter(user_id=request.user.id, is_ordered=True)
    orders_count = orders.count()

    userprofile = UserProfile.objects.get(user_id=request.user.id)
    context = {
        'orders_count': orders_count,
        'userprofile': userprofile,
    }
    return render (request, 'accounts/dashboard.html', context)


#___________________________________________________________  DEF FORGOTTPASSWORD
def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('signin')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('reset_password')
    else:
        return render(request, 'accounts/reset_password.html')


#___________________________________________________________  DEF MY_ORDERS
@login_required(login_url='signin')
def my_orders(request):
    orders = Order.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
    context = {
        'orders': orders,
    }
    return render(request, 'accounts/my_orders.html', context)


#___________________________________________________________  DEF EDIT_PROFILE
@login_required(login_url='signin')
def edit_profile(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, 'Your Profile has been updated!')
            return redirect('edit_profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'userprofile': userprofile,
    }
    return render(request, 'accounts/edit_profile.html', context)


#___________________________________________________________  DEF CHANGE_PASSOWRD
@login_required(login_url='signin')
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']

        user = Account.objects.get(username__exact=request.user.username)

        if new_password == confirm_new_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password is now updated!')
                return redirect('change_password')
            else:
                messages.error(request, 'Your current password is not correct!')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('change_password')

    return render(request, 'accounts/change_password.html')