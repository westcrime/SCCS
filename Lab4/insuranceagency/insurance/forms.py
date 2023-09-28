import datetime
import logging

import pytz
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import ModelForm

from .models import *


class EditObjectForm(ModelForm):
    class Meta:
        model = ObjectOfInsurance
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        logging.debug(f"имя - {name}")
        if name is None:
            raise ValidationError("Неправильный формат имени")
        for ch in name:
            if ch != ' ':
                return name
        return ValidationError("Неправильный формат имени")


class AddObjectForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = ObjectOfInsurance
        fields = ['name', 'photo', 'insured_risks', 'ins_cat', 'cost']

    def clean_cost(self):
        logging.basicConfig(filename='logging.log', encoding='utf-8', level=logging.DEBUG)
        cost = self.cleaned_data['cost']
        logging.debug(f"цена - {cost}")
        if cost <= 0:
            raise ValidationError("Неверный формат цены объекта!")
        logging.debug(f"цена из даты - {self.cleaned_data['cost']}")
        return cost

    def clean_name(self):
        name = self.cleaned_data['name']
        if name is None:
            raise ValidationError("Неправильный формат имени")
        for ch in name:
            if ch != ' ':
                return name
        return ValidationError("Неправильный формат имени")


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
        fields = ('username', 'phone_number', 'password1', 'password2')

    def clean_is_adult(self):
        is_adult = self.cleaned_data['is_adult']
        if not is_adult:
            raise ValidationError('Пользователь должен быть старше 18 лет!')


class LoginUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Логин' }))
    password = forms.CharField(label='Пароль', max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'пароль'}))


class MakeContractForm(ModelForm):
    class Meta:
        model = InsuranceContract
        fields = ['ins_object', 'time_end', 'ins_agent']

    def clean_time_end(self):
        now = datetime.datetime.now().replace(tzinfo=pytz.utc)
        time_end = self.cleaned_data['time_end']
        logging.basicConfig(filename='logging.log', encoding='utf-8', level=logging.DEBUG)
        if time_end <= now:
            raise ValidationError("Неправильная дата и время")
        logging.debug("Проверка на дату и время прошла успешно")
        return time_end
