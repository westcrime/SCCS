from django import template
from django.http import request

from insurance.models import *

register = template.Library()


@register.inclusion_tag('insurance/list_menu.html')
def show_menu(menu=None):
    menu = [{'title': "На главную", 'url_name': 'home'},
            {'title': "О сайте", 'url_name': 'about'},
            {'title': "Заключить договор", 'url_name': 'make_contract'},
            {'title': "Обратная связь", 'url_name': 'contact'}
            ]

    return {"menu": menu}


@register.inclusion_tag('insurance/list_sidebar.html')
def show_sidebar(menu=None, cat_selected="insurance_branches"):
    menu = [{'title': "Список филиалов", 'url_name': 'insurance_branches'},
            {'title': "Список договоров", 'url_name': 'insurance_contracts'},
            {'title': "Список агентов", 'url_name': 'insurance_agents'},
            {'title': "Список видов страхования", 'url_name': 'insurance_categories'}
            ]

    return {"menu": menu, "cat_selected": cat_selected}
