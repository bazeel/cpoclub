from django.views.generic import ListView
from library.models import Category, Doc


class DocList(ListView):

    model = Doc
    paginate_by = 10

    def get_queryset(self):
        qs = Doc.objects.filter(active=True)
        category = self.request.GET.get('category', False)

        if category:
            category = int(category)
            return qs.filter(category__pk=category)
        else:
            return qs

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DocList, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context