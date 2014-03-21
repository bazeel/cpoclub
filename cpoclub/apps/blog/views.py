import calendar
from django.shortcuts import render
from datetime import date
from django.views.generic import ListView
from .models import Record


class CustomRecordList(ListView):

    model = Record
    paginate_by = 1
    #queryset=Record.objects.filter(active=True)

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
    return render(request, 'blog/record_detail.html', {
        'qqq': 'qqq'})
