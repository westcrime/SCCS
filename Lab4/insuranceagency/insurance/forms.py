import datetime
import logging
import time
from django.utils import timezone
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm

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
        fields = ('username', 'phone_number', 'password1', 'password2')

    def clean_is_adult(self):
        is_adult = self.cleaned_data['is_adult']
        if not is_adult:
            raise ValidationError('Пользователь должен быть старше 18 лет!')


class LoginUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class MakeContractForm(ModelForm):
    class Meta:
        model = InsuranceContract
        fields = ['ins_object', 'time_end', 'ins_agent']

    def clean_time_end(self):
        now = datetime.datetime.now()
        logging.basicConfig(filename='logging.log', encoding='utf-8', level=logging.DEBUG)
        try:
            time_str = f"{self.cleaned_data['time_end'].year}-{self.cleaned_data['time_end'].month}-" \
                       f"{self.cleaned_data['time_end'].day} {self.cleaned_data['time_end'].hour}:" \
                       f"{self.cleaned_data['time_end'].minute}"
            logging.debug(str(time_str))
            time_end = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        except:
            raise ValidationError("Неправильный формат даты и времени")
        logging.debug(str(now))
        logging.debug(str(time_end))
        if time_end <= now:
            raise ValidationError("Неправильная дата и время")
        logging.debug("Проверка на дату и время прошла успешно")
        logging.debug(self.cleaned_data['time_end'])
        logging.debug(self.cleaned_data)
