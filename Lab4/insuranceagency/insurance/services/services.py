import datetime
import pytz
from django.contrib import auth

from ..models import *


def activate_contract(id: int):
    """Функция активации контракта"""
    if id is None:
        raise Exception("Activation of contract exception!")
    contract = InsuranceContract.objects.get(pk=id)
    contract.ins_agent.total_earning += contract.total_cost * contract.ins_agent.ins_branch.tariff_rate
    contract.ins_agent.save()
    contract.is_activated = True
    contract.save()


def delete_object_of_insurance(id: int, request):
    """Функция удаления объекта страховки конкретного пользователя"""
    if id is None:
        raise Exception("Deleting of object of insurance exception!")
    object = ObjectOfInsurance.objects.get(pk=id)
    if object.user.id == request.user.id:
        name = object.name
        object.delete()
        return name
    else:
        raise Exception("Deleting of object of insurance exception!")


def delete_contract_of_user(id: int, request):
    """Функция удаления контракта страховки конкретного пользователя"""
    if id is None:
        raise Exception("Deleting of object of insurance exception!")
    contract = InsuranceContract.objects.get(pk=id)
    if contract.ins_client.id == request.user.id:
        name_ob_object = contract.ins_object.name
        contract.delete()
        return name_ob_object
    else:
        raise Exception("Deleting of contract exception!")

def get_queryset_of_contracts(request):
    """Получение списка контрактов, отсортированного по выбранному пользователем признаку"""
     # Удаление контрактов, срок которых истек
    InsuranceContract.objects.filter(time_end__lte=datetime.datetime.now()).delete()
    sort_factor = request.GET.get('sort')
    available_sort_factors = ['time_create', 'time_end', 'total_cost']
    if sort_factor in available_sort_factors:
        return InsuranceContract.objects.filter(ins_client_id=request.user.id).order_by(sort_factor)
    return InsuranceContract.objects.filter(ins_client_id=request.user.id)


def get_queryset_of_categories(request):
    """Получение списка категорий, отсортированного по выбранному пользователем признаку"""
    sort_factor = request.GET.get('sort')
    available_sort_factors = ['name', 'ins_coef']
    if sort_factor in available_sort_factors:
        return InsuranceCategory.objects.order_by(sort_factor)
    return InsuranceCategory.objects.all()


def get_queryset_of_agents(request):
    """Получение списка агентов, отсортированного по выбранному пользователем признаку"""
    sort_factor = request.GET.get('sort')
    available_sort_factors = ['first_name', 'total_earning']
    if sort_factor in available_sort_factors:
        return InsuranceAgent.objects.order_by(sort_factor)
    return InsuranceAgent.objects.all()


def get_queryset_of_objects(request):
    """Получение списка объектов страхования, отсортированного по выбранному пользователем признаку"""
    sort_factor = request.GET.get('sort')
    available_sort_factors = ['name', 'cost']
    if sort_factor in available_sort_factors:
        return ObjectOfInsurance.objects.filter(user_id=request.user.id).order_by(sort_factor)
    return ObjectOfInsurance.objects.filter(user_id=request.user.id)


def make_contract(time_create, time_end, obj):
    """Оформление контракта, заполнение ее полей"""
    object_cost = obj.cost_with_all_coefs()
    if (time_end - time_create).days:
        total_cost = object_cost * (time_end - time_create).days
    else:
        total_cost = object_cost
    return total_cost