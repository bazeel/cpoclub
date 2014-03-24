from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from datetime import date
from django.views.generic import ListView
from account.models import UserProfile
from django.contrib.auth.models import User


class MembersList(ListView):

    model = User
    paginate_by = 10
    queryset = User.objects.filter(is_active=True)
    template_name='members/user_list.html'