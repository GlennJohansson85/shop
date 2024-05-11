#_________________________________________________________________________  ACCOUNTS/FORMS.PY
from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Choose a strong password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '<--- Same as this'
    }))

    class Meta:
        model   = Account
        fields  = ['first_name', 'last_name', 'email', 'password', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'David'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Hasselhoff'
        self.fields['email'].widget.attrs['placeholder'] = 'David.Hasselhoff@hotmail.com'
        self.fields['phone_number'].widget.attrs['placeholder'] = '+1 555-123-4567'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'