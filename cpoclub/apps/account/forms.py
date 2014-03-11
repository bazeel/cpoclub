from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile, InvitationCode


class CustomAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder':_('Username'), 'class':'span12'})
        self.fields['password'].widget = forms.TextInput(attrs={'placeholder':_('Password'), 'class':'span12', 
            'type':'password'})


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

    def clean_invitation_code(self):
        try:
            code = InvitationCode.objects.get(code=self.cleaned_data['invitation_code'])
        except InvitationCode.DoesNotExist:
            raise forms.ValidationError(_("Invitation code is incorrect"))

        try:
            profile = UserProfile.objects.get(invitation_code=code)
        except UserProfile.DoesNotExist:
            return self.cleaned_data['invitation_code']

        raise forms.ValidationError(_("A user with that invitation code already exists."))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("A user with that username already exists."))

    def clean_passwordconf(self):
        if 'password' in self.cleaned_data and 'passwordconf' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['passwordconf']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data['passwordconf']