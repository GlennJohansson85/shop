#_________________________________________________________________________  ACCOUNTS/FORMS.PY
from django import forms
from .models import Account


#___________________________________________________________  CLASS REGISTRATIONFORM
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Choose a strong password',
        'class': 'form-control',
    }))
    
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '<-- The one you created'
    }))

    class Meta:
        model  = Account
        fields = ['first_name', 'last_name', 'email', 'password', 'phone_number']


    def clean(self):
        cleaned_data     = super(RegistrationForm, self).clean()
        password         = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Passwords do not match."
            )
    
    def __init__(self, *args, **kwargs): # Use super for customization
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']   = 'David'
        self.fields['last_name'].widget.attrs['placeholder']    = 'Hasselhoff'
        self.fields['email'].widget.attrs['placeholder']        = 'David.Hasselhoff@hotmail.com'
        self.fields['phone_number'].widget.attrs['placeholder'] = '+1 555-123-4567'
        for field in self.fields:
            self.fields[field].widget.attrs['class']            = 'form-control'