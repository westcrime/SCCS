from django.urls import path, re_path
from .views import *

urlpatterns = [
                path('', home, name='home'),
                path('categories', categories, name='categories'),
                path('register/', register_user, name='register'),
                path('login/', login_user, name='login'),
                path('logout/', logout_user, name='logout'),
                path('delete_object/', delete_object, name='delete_object'),
                path('update_object/', update_object, name='update_object'),
                path('add_object/', AddObject.as_view(), name='add_object'),
                path('about/', about, name='about'),
                path('branches/', branches, name='branches'),
                path('contracts/', contracts, name='contracts'),
                path('make_contract/', MakeContractPage.as_view(), name='make_contract'),
                path('delete_contract/', delete_contract, name='delete_contract'),
                path('objects/', objects, name='objects'),
                path('agents/', agents, name='agents'),
                path('news/', news, name='news'),
                path('news_details/<int:news_id>/', news_details, name='news_details'),
                path('test/', test, name='test')
               ]
