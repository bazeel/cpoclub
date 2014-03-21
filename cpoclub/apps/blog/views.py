import calendar
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from datetime import date
from django.views.generic import ListView
from .models import Record, Comment


class CustomRecordList(ListView):

    model = Record
    paginate_by = 10

    def get_queryset(self):
        qs = Record.objects.filter(active=True)
        month = self.request.GET.get('month', False)
        year = self.request.GET.get('year', False)

        if month and year:
            month = int(month)
            year = int(year)

            last_day = calendar.monthrange(year, month)[1]

            start_date = date(year, month, 1)
            end_date = date(year, month, last_day)

            return qs.filter(date__range=(start_date, end_date))
        else:
            return qs


def record_detail(request, pk):
    obj = get_object_or_404(Record, pk=pk)

    u = request.user
    if not obj.public and not u.is_authenticated():
        return HttpResponseRedirect(reverse('account_login'))

    if request.method == 'POST' and u.is_authenticated():
        comment_msg = request.POST.get('comment', '')
        if comment_msg:
            comment_obj = Comment(user=u, record=obj, active=True, comment=comment_msg)
            comment_obj.save()

    return render(request, 'blog/record_detail.html', {
        'object': obj})
