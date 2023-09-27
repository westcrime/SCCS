from django.urls import path, re_path
from .views import *

urlpatterns = [
                path('', InsuranceCategoriesPage.as_view(), name='home'),
                path('logout/', logout_user_link, name='logout'),
                path('activate_contract/', activate_contract_link, name='activate_contract'),
                path('delete_object/', delete_object_link, name='delete_object'),
                path('edit_object/', edit_object, name='edit_object'),
                path('add_object/', AddObject.as_view(), name='add_object'),
                path('register/', RegisterUser.as_view(), name='register'),
                path('login/', LoginUser.as_view(), name='login'),
                path('insurance_branches/', InsuranceBranchesPage.as_view(), name='insurance_branches'),
                path('my_insurance_contracts/', InsuranceContractsPage.as_view(), name='my_insurance_contracts'),
                path('make_contract/', MakeContractPage.as_view(), name='make_contract'),
                path('objects/', ObjectsOfInsurancePage.as_view(), name='objects'),
                path('list_agents/', InsuranceAgentsPage.as_view(), name='list_agents'),
                path('', InsuranceCategoriesPage.as_view(), name='insurance_categories'),
               ]
