from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .api.activity import ActivityService
from .api.joke import JokeService
from .services.services import *
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
import logging
# from api.joke import JokeService
# from api.activity import ActivityService
from .forms import RegisterUserForm, MakeContractForm, AddObjectForm, EditObjectForm
from .models import *


def login_user(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('Пароль или/и имя пользователя не верны, попробуйте еще раз...'))
            return redirect('login')

    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'authentication/login.html')


def logout_user(request):
    auth.logout(request)
    messages.success(request, ('Вы успешно вышли из своего профиля...'))
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Пользователь успешно зарегистрирован...")
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'authentication/register.html', {
        'form': form,
    })


def activate_contract_link(request):
    id = request.GET.get('id')
    activate_contract(id)
    messages.success(request, "Вы активировали страховку!")
    return redirect('home')


def delete_object_link(request):
    id = request.GET.get('id')
    try:
        name = delete_object_of_insurance(id, request)
    except:
        messages.warning(request, f"Возникли ошибки при удалении: {name}!")
        return redirect('insurance_objects')
    messages.success(request, f"Вы успешно удалили объект: {name}!")
    return redirect('insurance_objects')


def about(request):
    context = {'active_contracts': InsuranceContract.objects.filter(is_activated=True).count()}
    for i in range(0, 3):
        joke = JokeService.get_random_joke()
        context[f'joke{i + 1}'] = joke['setup'] + '-' + joke['punchline']
        context[f'activity{i + 1}'] = ActivityService.get_random_activity()['activity']
    return render(request, 'about.html', context)


class InsuranceContractsPage(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = InsuranceContract
    template_name = 'list_contracts.html'
    context_object_name = 'contracts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Ваши страховочные контракты")
        context['cat_selected'] = 'my_insurance_contracts'
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return get_queryset_of_contracts(self.request)


class InsuranceCategoriesPage(ListView):
    model = InsuranceCategory
    template_name = 'index.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        joke = JokeService.get_random_joke()
        activity = ActivityService.get_random_activity()
        context['joke'] = joke['setup'] + ' ' + joke['punchline']
        context['activity'] = activity['activity']
        context['cat_selected'] = ''
        return dict(list(context.items()))

    def get_queryset(self):
        return get_queryset_of_categories(self.request)


class InsuranceBranchesPage(ListView):
    model = InsuranceBranch
    template_name = 'insurance_branches.html'
    context_object_name = 'branches'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Филиалы нашего агенства")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return InsuranceBranch.objects.all()


class InsuranceAgentsPage(ListView):
    model = InsuranceAgent
    template_name = 'insurance_agents.html'
    context_object_name = 'agents'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Агенты нашей компании")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return get_queryset_of_agents(self.request)


class ObjectsOfInsurancePage(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = ObjectOfInsurance
    template_name = 'insurance_objects.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Ваши зарегистрированные объекты")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return get_queryset_of_objects(self.request)


class AddObject(LoginRequiredMixin, CreateView):
    login_url = 'login'
    form_class = AddObjectForm
    template_name = 'add_object.html'
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


def update_object(request):
    id = request.GET.get('id')
    object = ObjectOfInsurance.objects.get(id=id)
    if object.user.id == request.user.id:
        if request.method == 'POST':
            form = EditObjectForm(request.POST, instance=object)
            if form.is_valid():
                form.save()
                return redirect('insurance_objects')
        else:
            form = EditObjectForm(instance=object, )
            return render(request, 'edit_object.html', {'form': form})
    else:
        raise Exception(f"Cant edit ({object.user} - objects user id, {request.user.id} - current users id)")


class MakeContractPage(LoginRequiredMixin, CreateView):
    login_url = 'login'
    form_class = MakeContractForm
    template_name = 'make_contract.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Оформление страховки")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        make_contract(self.request, form)
        messages.success(self.request, "Вы оформили страховку, можете узнать ее цену и активировать в МОИХ ДОГОВОРАХ")
        return redirect('home')
