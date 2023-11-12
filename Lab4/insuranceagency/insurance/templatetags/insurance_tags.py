from django import template

register = template.Library()


@register.inclusion_tag('navbar_menu.html')
def show_navbar_menu(menu=None, user=None):
    menu = [
        {'title': "На главную", 'url_name': 'home'},
        {'title': "Виды страхования", 'url_name': 'categories'},
        {'title': "Агенты", 'url_name': 'agents'},
        {'title': "Филиалы", 'url_name': 'branches'},
        {'title': "Новости", 'url_name': 'news'},
        {'title': "О сайте", 'url_name': 'about'}
            ]
    user_menu = [
        {'title': "Список объектов", 'url_name': 'objects'},
        {'title': "Список договоров", 'url_name': 'contracts'},
        {'title': "Заключить договор", 'url_name': 'make_contract'},
        {'title': "Выйти из профиля", 'url_name': 'logout'},
    ]

    return {"menu": menu, "user_menu": user_menu, "user": user}