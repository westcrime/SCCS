from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
import logging
from .forms import RegisterUserForm
from .models import *
from insurance.utils import DataMixin


def logout_user(request):
    logout(request)
    return redirect('home')


class InsuranceCategories(DataMixin, ListView):
    model = InsuranceCategory
    template_name = 'insurance/index.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        if self.request.GET.get('sort') == 'name':
            return InsuranceCategory.objects.order_by('name')
        if self.request.GET.get('sort') == 'ins_coef':
            return InsuranceCategory.objects.order_by('ins_coef')
        return InsuranceCategory.objects.all()


class InsuranceBranches(DataMixin, ListView):
    model = InsuranceBranch
    template_name = 'insurance/insurancebranches.html'
    context_object_name = 'branches'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Филиалы нашего агенства")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return InsuranceBranch.objects.all()


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'insurance/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        logging.info("Пользователь успешно зарегистрирован")
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'insurance/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        logging.info("Пользователь успешно авторизован")
        return reverse_lazy('home')
