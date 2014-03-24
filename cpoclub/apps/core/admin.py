from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from core.forms import PageForm


class PageAdmin(FlatPageAdmin):
    """
    Page Admin
    """
    form = PageForm

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PageAdmin)