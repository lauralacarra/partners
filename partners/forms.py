from django import forms  
from .models import Partner
from django.utils.translation import ugettext_lazy as _


class PartnerForm(forms.ModelForm):

    class Meta:
        model = Partner
        fields = ('name', 'lastname', 'dni', 'email', 'address',
                  'postal_code', 'city', 'state', 'country', )
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Name'),
            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('last name'),
            }),
            'dni': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'DNI',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _('Email'),
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Address'),
            }),
            'postal_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('CP'),
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('City'),
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('State')
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Country'),
            }),
        }


class PartnerHTMLForm(forms.ModelForm):

    class Meta:
        model = Partner
        fields = ('name', 'lastname', 'dni', 'email', 'address',
                  'postal_code', 'city', 'state', 'country', )



class PartnerSimpleForm(forms.ModelForm):

    class Meta:
        model = Partner
        exclude = ('created_date', )


