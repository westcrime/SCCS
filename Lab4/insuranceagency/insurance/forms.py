import logging

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    phone_regex = RegexValidator(regex=r'^\+37529\d{7}$',
                                 message="Телефонный номер должен быть введен в формате: '+37529xxxxxxx'. Разрешено "
                                         "до 15 цифр")
    phone_number = forms.CharField(label='Номер телефона', validators=[phone_regex], max_length=17,
                                   widget=forms.TextInput(attrs={'class': 'form-input'}))  # Validators should be a list
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    is_adult = forms.BooleanField(label='Я подтверждаю, что мне больше 18')

    class Meta:
        model = User
        fields = ('username','phone_number' , 'password1', 'password2')

    def clean_is_adult(self):
        is_adult = self.cleaned_data['is_adult']
        if not is_adult:
            raise ValidationError('Пользователь должен быть старше 18 лет!')


class LoginUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
