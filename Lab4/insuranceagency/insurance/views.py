import datetime
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
import logging
from .forms import RegisterUserForm, MakeContractForm
from .models import *
from insurance.utils import DataMixin


def logout_user(request):
    logout(request)
    return redirect('home')


def activate_contract(request):
    get = request.GET.get('id')
    if get is not None:
        contract = InsuranceContract.objects.get(pk=get)
        contract.ins_agent.total_earning += contract.total_cost * contract.ins_agent.ins_branch.tariff_rate
        contract.ins_agent.save()

        contract.is_activated = True
        contract.save()
        messages.success(request, "Вы активировали страховку!")
        return redirect('home')


def delete_object(request):
    get = request.GET.get('id')
    if get is not None:
        object = ObjectOfInsurance.objects.get(pk=get)
        name = object.name
        object.delete()
        messages.success(request, f"Вы удалили: {name}!")
        return redirect('home')


class InsuranceContracts(LoginRequiredMixin, DataMixin, ListView):
    login_url = 'login'
    model = InsuranceContract
    template_name = 'insurance/list_contracts.html'
    context_object_name = 'contracts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Ваши страховочные контракты")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        InsuranceContract.objects.filter(time_end__lte=datetime.datetime.now()).delete()
        if self.request.GET.get('sort') == 'time_create':
            return InsuranceContract.objects.filter(ins_client_id=self.request.user.id).order_by('time_create')
        elif self.request.GET.get('sort') == 'time_end':
            return InsuranceContract.objects.filter(ins_client_id=self.request.user.id).order_by('time_end')
        elif self.request.GET.get('sort') == 'total_cost':
            return InsuranceContract.objects.filter(ins_client_id=self.request.user.id).order_by('total_cost')
        else:
            return InsuranceContract.objects.filter(ins_client_id=self.request.user.id)


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


class ObjectsOfInsurance(LoginRequiredMixin, DataMixin, ListView):
    login_url = 'login'
    model = ObjectOfInsurance
    template_name = 'insurance/list_objects.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Ваши зарегистрированные объекты")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        if self.request.GET.get('sort') == 'name':
            return ObjectOfInsurance.objects.filter(user_id=self.request.user.id).order_by('name')
        if self.request.GET.get('sort') == 'cost':
            return ObjectOfInsurance.objects.filter(user_id=self.request.user.id).order_by('cost')
        return ObjectOfInsurance.objects.filter(user_id=self.request.user.id)


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


class MakeContract(LoginRequiredMixin, DataMixin, CreateView):
    login_url = 'login'
    form_class = MakeContractForm
    template_name = 'insurance/make_contract.html'
    success_url = reverse_lazy('home')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Оформление страховки")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        logging.basicConfig(filename='logging.log', encoding='utf-8', level=logging.DEBUG)
        logging.debug(form.cleaned_data)
        data = self.request.POST.dict()
        logging.debug(data)
        time_end = datetime.datetime.strptime(data['time_end'], "%d.%m.%Y")
        contract = form.save(commit=False)
        contract.user = self.request.user
        contract.time_create = datetime.datetime.now()
        obj = form.cleaned_data['ins_object']
        object_cost = obj.cost
        if obj.insured_risks == "Низкие":
            object_cost_with_risk = object_cost * 0.033
        elif obj.insured_risks == "Нормальные":
            object_cost_with_risk = object_cost * 0.066
        else:
            object_cost_with_risk = object_cost * 0.1
        object_cost_with_cat = object_cost_with_risk * obj.ins_cat.ins_coef
        logging.debug(f"клин дата - {form.cleaned_data}")
        logging.debug(contract.time_create)
        logging.debug(time_end)
        if (time_end - contract.time_create).days:
            contract.total_cost = object_cost_with_cat * (time_end - contract.time_create).days
        else:
            contract.total_cost = object_cost_with_cat
        contract.ins_client = self.request.user
        contract.time_end = time_end

        contract = form.save()
        messages.success(self.request, "Вы оформили страховку, можете узнать ее цену и активировать в МОИХ ДОГОВОРАХ")
        return redirect('home')

