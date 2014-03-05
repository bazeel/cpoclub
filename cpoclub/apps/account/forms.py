from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.utils.translation import ugettext_lazy as _


class UserForm(forms.ModelForm):
    invitation_code = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
            super(UserForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].required = True
            self.fields['last_name'].required = True
            self.fields['email'].required = True
            self.fields['username'].widget = forms.TextInput(attrs={'placeholder': _('Username'), 'class': 'span12'})
            self.fields['email'].widget = forms.TextInput(attrs={'placeholder': 'E-mail', 'class': 'span12'})
            self.fields['invitation_code'].widget = forms.TextInput(attrs={'placeholder': _('Member number'), 
                'class': 'span12'}) 
            self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': _('First name'), 'class': 'span12'})
            self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': _('Last name'), 'class': 'span12'})

    '''
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data
    '''