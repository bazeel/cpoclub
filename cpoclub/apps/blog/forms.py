from django import forms
from django.utils.translation import ugettext_lazy as _


class RecAddForm(forms.Form):
    title = forms.CharField(widget = forms.TextInput(attrs={'placeholder':_('Title'), 'class':'span12'}),
        required=True)
    public = forms.BooleanField(required=False, initial=True)
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder':_('Your record'), 
                'class':'input-xxlarge',
                'rows':'20'
            }),
        required=True)
