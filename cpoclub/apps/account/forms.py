from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.utils.translation import ugettext_lazy as _


class UserForm(forms.ModelForm):
    invitation_code = forms.CharField(required=True)
    passwordconf = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
            super(UserForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].required = True
            self.fields['last_name'].required = True
            self.fields['email'].required = True
            self.fields['username'].widget = forms.TextInput(attrs={'placeholder':_('Username'), 'class':'span12'})
            self.fields['password'].widget = forms.TextInput(attrs={'placeholder':_('Password'), 'class':'span12', 
                'type':'password'})
            self.fields['passwordconf'].widget = forms.TextInput(attrs={'placeholder':_('Confirm password'), 
                'class':'span12', 'type':'password'})
            self.fields['email'].widget = forms.TextInput(attrs={'placeholder':'E-mail', 'class':'span12', 
                'type':'email'})
            self.fields['invitation_code'].widget = forms.TextInput(attrs={'placeholder':_('Invitation code'), 
                'class':'span12'}) 
            self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': _('Firstname'), 'class': 'span12'})
            self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': _('Lastname'), 'class': 'span12'})

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        
        """
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("A user with that username already exists."))

    def clean_passwordconf(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        
        """
        if 'password' in self.cleaned_data and 'passwordconf' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['passwordconf']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data['passwordconf']