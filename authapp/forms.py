import hashlib
import random

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import GiftUser
from address.forms import AddressField


class GiftUserLoginForm(AuthenticationForm):
    class Meta:
        model = GiftUser
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super(GiftUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name


class GiftUserRegisterForm(UserCreationForm):
    class Meta:
        model = GiftUser
        fields = ('first_name', 'last_name', 'password1', 'password2', 'email', 'age', 'avatar', 'gender')
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GiftUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    # def clean_age(self):
    #     data = self.cleaned_data['age']
    #     if data < 18:
    #         raise forms.ValidationError("Вы слишком молоды!")
    #
    #     return data

    # def save(self, commit=True):
    #     user = super().save(commit)
    #     user.is_active = False
    #
    #     salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
    #     user.active_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
    #     user.save()
    #     return user
    #


class GiftUserEditForm(UserChangeForm):
    class Meta:
        model = GiftUser
        fields = ('first_name', 'middle_name', 'last_name', 'gender', 'address_list', 'age', 'password', 'avatar')

    def __init__(self, *args, **kwargs):
        super(GiftUserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    # def clean_age(self):
    #     data = self.cleaned_data['age']
    #     if data < 18:
    #         raise forms.ValidationError("Вы слишком молоды!")

    #    return data


class PersonForm(forms.Form):
    address = AddressField()
