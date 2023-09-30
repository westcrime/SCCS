from django import template

register = template.Library()


@register.inclusion_tag('main_menu.html')
def show_menu(menu=None, user=None):
    menu = [{'title': "На главную", 'url_name': 'home'},
            {'title': "Заключить договор", 'url_name': 'make_contract'},
            {'title': "О сайте", 'url_name': 'about'}
            ]

    return {"menu": menu, "user": user}


@register.inclusion_tag('second_menu.html')
def show_second_menu(menu=None, cat_selected="insurance_branches"):
    menu = [{'title': "Список филиалов", 'url_name': 'branches'},
            {'title': "Список объектов", 'url_name': 'objects'},
            {'title': "Список договоров", 'url_name': 'contracts'},
            {'title': "Список агентов", 'url_name': 'agents'},
            {'title': "Виды страхования", 'url_name': 'categories'}
            ]

    return {"second_menu": menu, "cat_selected": cat_selected}
