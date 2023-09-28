from django.urls import path, re_path
from .views import *

urlpatterns = [
                path('home', categories, name='home'),
                path('categories', categories, name='categories'),
                path('register/', register_user, name='register'),
                path('login/', login_user, name='login'),
                path('logout/', logout_user, name='logout'),
                path('activate_contract/', activate_contract_link, name='activate_contract'),
                path('delete_object/', delete_object_link, name='delete_object'),
                path('edit_object/', edit_object, name='edit_object'),
                path('add_object/', AddObject.as_view(), name='add_object'),
                path('about/', about, name='about'),
                path('branches/', branches, name='branches'),
                path('contracts/', contracts, name='contracts'),
                path('make_contract/', MakeContractPage.as_view(), name='make_contract'),
                path('objects/', objects, name='objects'),
                path('agents/', agents, name='agents'),
               ]
