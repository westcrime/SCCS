from django.db.models import Count

from .models import *

menu = [{'title': "На главную", 'url_name': 'home'},
            {'title': "О сайте", 'url_name': 'about'},
            {'title': "Заключить договор", 'url_name': 'make_contract'},
            {'title': "Обратная связь", 'url_name': 'contact'}]

sidebar_menu = [{'title': "Список филиалов", 'url_name': 'insurance_branches'},
            {'title': "Список моих договоров", 'url_name': 'my_insurance_contracts'},
            {'title': "Список агентов", 'url_name': 'insurance_agents'},
            {'title': "Список видов страхования", 'url_name': ''},
            {'title': "Список моих объектов страхования", 'url_name': 'objects'}]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs

        user_sidebar_menu = sidebar_menu.copy()
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)
            user_sidebar_menu.pop(1)
            user_sidebar_menu.pop(1)
            user_sidebar_menu.pop(2)

        context['menu'] = user_menu

        context['sidebar_menu'] = user_sidebar_menu
        if 'cat_selected' not in context:
            context['cat_selected'] = user_sidebar_menu[0]['title']
        return context
