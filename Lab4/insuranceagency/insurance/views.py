from .services.services import *
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
import logging
from insurance.api.joke import JokeService
from insurance.api.activity import ActivityService
from insurance.forms import RegisterUserForm, MakeContractForm, AddObjectForm, EditObjectForm
from insurance.models import *
from insurance.utils import DataMixin


def logout_user_link(request):
    logout(request)
    return redirect('home')


def activate_contract_link(request):
    id = request.GET.get('id')
    activate_contract(id)
    messages.success(request, "Вы активировали страховку!")
    return redirect('home')


def delete_object_link(request):
    id = request.GET.get('id')
    name = delete_object_of_insurance(id)
    messages.success(request, f"Вы успешно удалили объект: {name}!")
    return redirect('objects')


class InsuranceContractsPage(LoginRequiredMixin, DataMixin, ListView):
    login_url = 'login'
    model = InsuranceContract
    template_name = 'insurance/list_contracts.html'
    context_object_name = 'contracts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Ваши страховочные контракты")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return get_queryset_of_contracts(self.request)


class InsuranceCategoriesPage(DataMixin, ListView):
    model = InsuranceCategory
    template_name = 'insurance/index.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        joke = JokeService.get_random_joke()
        activity = ActivityService.get_random_activity()
        # context['joke'] = joke['setup'] + ' ' + joke['punchline']
        # context['activity'] = activity['activity']
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return get_queryset_of_categories(self.request)


class InsuranceBranchesPage(DataMixin, ListView):
    model = InsuranceBranch
    template_name = 'insurance/insurancebranches.html'
    context_object_name = 'branches'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Филиалы нашего агенства")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return InsuranceBranch.objects.all()


class InsuranceAgentsPage(DataMixin, ListView):
    model = InsuranceAgent
    template_name = 'insurance/list_agents.html'
    context_object_name = 'agents'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Агенты нашей компании")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return get_queryset_of_agents(self.request)


class ObjectsOfInsurancePage(LoginRequiredMixin, DataMixin, ListView):
    login_url = 'login'
    model = ObjectOfInsurance
    template_name = 'insurance/list_objects.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Ваши зарегистрированные объекты")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return get_queryset_of_objects(self.request)


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


class AddObject(LoginRequiredMixin, DataMixin, CreateView):
    login_url = 'login'
    form_class = AddObjectForm
    template_name = 'insurance/add_object.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление нового объекта")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user_id = self.request.user.pk
        form.save()
        logging.info("Объект успешно Добавлен")
        return redirect('home')


def edit_object(request):
    id = request.GET.get('id')
    object = ObjectOfInsurance.objects.get(id=id)
    if request.method == 'POST':
        form = EditObjectForm(request.POST, instance=object)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('objects')
    else:
        form = EditObjectForm(instance=object,)
        return render(request, 'insurance/edit_object.html', {'form': form})


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


class MakeContractPage(LoginRequiredMixin, DataMixin, CreateView):
    login_url = 'login'
    form_class = MakeContractForm
    template_name = 'insurance/make_contract.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Оформление страховки")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        make_contract(self.request, form)
        messages.success(self.request, "Вы оформили страховку, можете узнать ее цену и активировать в МОИХ ДОГОВОРАХ")
        return redirect('home')

