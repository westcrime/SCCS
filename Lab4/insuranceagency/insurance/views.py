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
from django.contrib.auth.decorators import login_required
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

        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, ('Пароль или/и имя пользователя не верны, попробуйте еще раз...'))
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


def about(request):
    context = {'active_contracts': InsuranceContract.objects.count()}
    for i in range(0, 3):
        joke = JokeService.get_random_joke()
        context[f'joke{i + 1}'] = joke['setup'] + '-' + joke['punchline']
        context['title'] = 'О сайте'
        context['cat_selected'] = 'about'
        context[f'activity{i + 1}'] = ActivityService.get_random_activity()['activity']
    return render(request, 'about.html', context)


@login_required
def contracts(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    context = {}
    context['title'] = 'Страховки'
    context['cat_selected'] = 'contracts'
    context['contracts'] = get_queryset_of_contracts(request)
    return render(request, 'contracts.html', context)


def home(request):
    context = {}
    joke = JokeService.get_random_joke()
    activity = ActivityService.get_random_activity()
    context['joke'] = joke['setup'] + ' ' + joke['punchline']
    context['activity'] = activity['activity']
    context['cat_selected'] = 'home'
    context['title'] = 'Главная страница'
    context['categories'] = get_queryset_of_categories(request)
    return render(request, 'categories.html', context)


def categories(request):
    context = {}
    joke = JokeService.get_random_joke()
    activity = ActivityService.get_random_activity()
    context['joke'] = joke['setup'] + ' ' + joke['punchline']
    context['activity'] = activity['activity']
    context['cat_selected'] = 'categories'
    context['title'] = 'Категории страхования'
    context['categories'] = get_queryset_of_categories(request)
    return render(request, 'categories.html', context)


def branches(request):
    context = {}
    context['cat_selected'] = 'branches'
    context['title'] = 'Филиалы'
    context['branches'] = InsuranceBranch.objects.all()
    return render(request, 'branches.html', context)


def agents(request):
    context = {}
    context['cat_selected'] = 'agents'
    context['title'] = 'Агенты'
    context['agents'] = get_queryset_of_agents(request)
    return render(request, 'agents.html', context)


@login_required
def objects(request):
    context = {}
    context['cat_selected'] = 'objects'
    context['title'] = 'Объекты'
    context['objects'] = get_queryset_of_objects(request)
    return render(request, 'objects.html', context)


class AddObject(LoginRequiredMixin, CreateView):
    login_url = 'login'
    form_class = AddObjectForm
    template_name = 'add_object.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user_id = self.request.user.pk
        form.save()
        logging.info("Объект успешно Добавлен")
        return redirect('home')


@login_required
def update_object(request):
    id = request.GET.get('id')
    object = ObjectOfInsurance.objects.get(id=id)
    if object.user.id == request.user.id:
        if request.method == 'POST':
            form = EditObjectForm(request.POST, instance=object)
            if form.is_valid():
                form.save()
                return redirect('objects')
        else:
            form = EditObjectForm(instance=object, )
            return render(request, 'update_object.html', {'form': form})
    else:
        raise Exception(f"Cant edit ({object.user} - objects user id, {request.user.id} - current users id)")


@login_required
def delete_object(request):
    id = request.GET.get('id')
    try:
        object = ObjectOfInsurance.objects.get(id=id)
        if object.user.id == request.user.id:
            name = delete_object_of_insurance(id, request)
    except:
        messages.warning(request, f"Возникли ошибки при удалении: {name}!")
        return redirect('insurance_objects')
    messages.success(request, f"Вы успешно удалили объект: {name}!")
    return redirect('objects')


class MakeContractPage(LoginRequiredMixin, CreateView):
    login_url = 'login'
    form_class = MakeContractForm
    template_name = 'make_contract.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        form.instance.time_create = datetime.datetime.now().replace(tzinfo=pytz.utc)
        form.instance.ins_client = self.request.user
        form.instance.total_cost = make_contract(form.instance.time_create, form.instance.time_end, form.instance.ins_object)
        form.save()
        messages.success(self.request, f"Вы успешно застраховали объект {(form.cleaned_data['ins_object']).name}")
        return redirect('contracts')
