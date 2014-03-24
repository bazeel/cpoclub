from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
## OOPS this is a custom widget that works for initializing
## tinymce instances on stacked and tabular inlines
## for flatpages, just use the tinymce packaged one.
#from content.widgets import TinyMCE 
from tinymce.widgets import TinyMCE


class PageForm(FlatpageForm):

    class Meta:
        model = FlatPage
        widgets = {
            'content' : TinyMCE(attrs={'cols': 100, 'rows': 15}),
        }