from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    '''
    Form class is used to create and update orders in the Django application.
    It is based on the Order model.
    '''
    class Meta:
        model   = Order
        fields  = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'address_line_1',
            'address_line_2',
            'country',
            'city',
            'order_note',
            ]
