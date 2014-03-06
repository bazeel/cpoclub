from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import *
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
#from django.contrib.sites.models import Site

from .forms import UserForm


def login_view(request):

    entered = False
    disabled_account = False
    invalid_login = False
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            d = form.cleaned_data
            user = authenticate(username=d['username'], password=d['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    entered = True
                else:
                    disabled_account = True # Return a 'disabled account' error message
            else:
                invalid_login = True # Return an 'invalid login' error message.
    else:
        form = AuthenticationForm()

    return render(request, 'account/login_form_ajax.html', {
        'form': form,
        'entered': entered,
        'disabled_account': disabled_account,
        'invalid_login': invalid_login})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def register(request):
    user_form = UserForm(prefix='user_form')
    success = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user_data = user_form.save(commit=False)
            print vars(user_form)
            try:
                user = User.objects.create_user(user_data.username, user_data.email, user_data.password)
            except Exception:
                pass
            else:
                pass

    return render(request, 'account/register.html', {
            'user_form': user_form,
            'success': success,
        })
    '''
    user_form = UserForm(prefix='user_form')x
    user_profile_form = UserProfileForm(prefix='user_profile_form')
    success = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST, prefix='user_form')
        user_profile_form = UserProfileForm(data=request.POST, prefix='user_profile_form')
        if user_form.is_valid() and user_profile_form.is_valid():
            user_data = user_form.save(commit=False)
            user_profile = user_profile_form.save(commit=False)
            try:
                user = User.objects.create_user(user_data.username, user_data.email, user_data.password)
            except Exception:
                pass
            else:
                user.first_name = user_data.first_name
                user.save()
                user_profile_obj = UserProfile(user=user, country=user_profile.country, gender=user_profile.gender)
                user_profile_obj.save()
                success = True
                current_site = Site.objects.get_current()
                subject = render_to_string('account/mail/subject.txt', {'site': current_site})
                body = render_to_string('account/mail/body.txt', {'object': user_data})
                recipients = [user_data.email,]
                send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, recipients)


    return render(request, 'account/register.html', {
        'user_form': user_form,
        'user_profile_form': user_profile_form,
        'success': success,})
    '''
