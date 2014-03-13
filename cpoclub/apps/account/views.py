from django.template import RequestContext
#from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import *
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
#from django.contrib.sites.models import Site

from .forms import UserForm, CustomAuthenticationForm
from .models import InvitationCode, UserProfile


def login_view(request):
    u = request.user
    if u.is_authenticated():
        return HttpResponseRedirect(reverse('index'))

    disabled_account = False
    invalid_login = False
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            d = form.cleaned_data
            user = authenticate(username=d['username'], password=d['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))

                else:
                    disabled_account = True # Return a 'disabled account' error message
            else:
                invalid_login = True # Return an 'invalid login' error message.
    else:
        form = CustomAuthenticationForm()

    return render(request, 'account/login.html', {
        'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    u = request.user
    if u.is_authenticated():
        return HttpResponseRedirect(reverse('index'))

    user_form = UserForm()
    success = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user_data = user_form.cleaned_data
            try:
                user = User.objects.create_user(
                    user_data['username'],
                    user_data['email'], 
                    user_data['password'])
            except Exception:
                pass
            else:
                # TODO: move InvitationCode, UserProfile to custom User.create_user method
                code = InvitationCode.objects.get(code=user_data['invitation_code'])
                profile = UserProfile(user=user, invitation_code=code)
                profile.save()
                user.first_name = user_data['first_name']
                user.last_name = user_data['last_name']
                user.save()
                success = True
                user_form = UserForm()
                # TODO: send mail to user

    return render(request, 'account/register.html', {
        'user_form': user_form,
        'success': success,
    })