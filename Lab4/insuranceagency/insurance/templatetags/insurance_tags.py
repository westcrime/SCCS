from django import template

register = template.Library()


@register.inclusion_tag('main_menu.html')
def show_menu(menu=None):
    menu = [{'title': "На главную", 'url_name': 'home'},
            {'title': "Заключить договор", 'url_name': 'make_contract'},
            {'title': "О сайте", 'url_name': 'about'}
            ]

    return {"menu": menu}


@register.inclusion_tag('second_menu.html')
def show_second_menu(menu=None, cat_selected="insurance_branches"):
    menu = [{'title': "Список филиалов", 'url_name': 'insurance_branches'},
            {'title': "Список объектов", 'url_name': 'insurance_objects'},
            {'title': "Список договоров", 'url_name': 'my_insurance_contracts'},
            {'title': "Список агентов", 'url_name': 'insurance_agents'},
            {'title': "Список видов страхования", 'url_name': 'insurance_categories'}
            ]

    return {"second_menu": menu, "cat_selected": cat_selected}
