from django.urls import path, re_path
from .views import *

urlpatterns = [
                path('', InsuranceCategories.as_view(), name='home'),
                path('logout/', logout_user, name='logout'),
                path('', InsuranceCategories.as_view(), name='about'),
                path('', InsuranceCategories.as_view(), name='make_contract'),
                path('', InsuranceCategories.as_view(), name='contact'),
                path('register/', RegisterUser.as_view(), name='register'),
                path('login/', LoginUser.as_view(), name='login'),
                path('insurance_branches/', InsuranceBranches.as_view(), name='insurance_branches'),
                path('insurance_contracts/', InsuranceCategories.as_view(), name='insurance_contracts'),
                path('my_insurance_contracts/', InsuranceCategories.as_view(), name='my_insurance_contracts'),
                path('insurance_agents/', InsuranceCategories.as_view(), name='insurance_agents'),
                path('', InsuranceCategories.as_view(), name='insurance_categories'),
               ]
