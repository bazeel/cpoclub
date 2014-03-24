from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from datetime import date
from django.views.generic import ListView
from account.models import UserProfile
from django.contrib.auth.models import User

from blog.models import Record


class MembersList(ListView):

    model = User
    paginate_by = 10
    queryset = User.objects.filter(is_active=True)
    template_name='members/user_list.html'


class UserRecList(ListView):

    paginate_by = 1
    

    def get_template_names(self):
        template_name = 'members/user_rec_list.html'
        return template_name

    def get_queryset(self, **kwargs):
        user_pk = self.kwargs['pk']
        qs = Record.objects.filter(active=True, user__pk=user_pk)
        return qs

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UserRecList, self).get_context_data(**kwargs)
        user_pk = self.kwargs['pk']
        user = User.objects.get(pk=user_pk)
        context['object_user'] = user
        return context