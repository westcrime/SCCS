from django.urls import path, re_path
from .views import *

urlpatterns = [
                path('', InsuranceCategories.as_view(), name='home'),
                path('logout/', logout_user, name='logout'),
                path('', InsuranceCategories.as_view(), name='about'),
                path('', InsuranceCategories.as_view(), name='make_contract'),
                path('activate_contract/', activate_contract, name='activate_contract'),
                path('delete_object/', delete_object, name='delete_object'),
                path('', InsuranceCategories.as_view(), name='contact'),
                path('register/', RegisterUser.as_view(), name='register'),
                path('login/', LoginUser.as_view(), name='login'),
                path('insurance_branches/', InsuranceBranches.as_view(), name='insurance_branches'),
                path('my_insurance_contracts/', InsuranceContracts.as_view(), name='my_insurance_contracts'),
                path('make_contract/', MakeContract.as_view(), name='make_contract'),
                path('objects/', ObjectsOfInsurance.as_view(), name='objects'),
                path('insurance_agents/', InsuranceCategories.as_view(), name='insurance_agents'),
                path('', InsuranceCategories.as_view(), name='insurance_categories'),
               ]
