from django import template
from django.db import connection
from blog.models import Record
from datetime import date

register = template.Library()


@register.inclusion_tag('blog/tags/latest_rec_list.html')
def latest_rec_list():
    qs = Record.objects.filter(active=True)
    try:
        qs = qs[:5]
    except Exception:
        qs = []

    return {'object_list': qs }


@register.inclusion_tag('blog/tags/latest_rec_index.html')
def latest_rec_index():
    qs = Record.objects.filter(active=True)
    try:
        qs = qs[:3]
    except Exception:
        qs = []

    return {'object_list': qs }


@register.inclusion_tag('blog/tags/rec_archive.html')
def rec_archive():
   qs = Record.objects.filter(active=True)
   archive = {}

   date_field = 'date'

   years = qs.dates(date_field, 'year')[::-1]
   for date_year in years:
       months = qs.filter(date__year=date_year.year).dates(date_field, 'month')
       archive[date_year] = months

   archive = sorted(archive.items(), reverse=True)

   return {'archive': archive}
