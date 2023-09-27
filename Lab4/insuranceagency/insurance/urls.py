from django.urls import path, re_path
from .views import *

urlpatterns = [
                path('', InsuranceCategoriesPage.as_view(), name='home'),
                path('', InsuranceCategoriesPage.as_view(), name='insurance_categories'),
                path('register/', register_user, name='register'),
                path('login/', login_user, name='login'),
                path('logout/', logout_user, name='logout'),
                path('activate_contract/', activate_contract_link, name='activate_contract'),
                path('delete_object/', delete_object_link, name='delete_object'),
                path('edit_object/', edit_object, name='edit_object'),
                path('add_object/', AddObject.as_view(), name='add_object'),
                path('about/', about, name='about'),
                path('insurance_branches/', InsuranceBranchesPage.as_view(), name='insurance_branches'),
                path('my_insurance_contracts/', InsuranceContractsPage.as_view(), name='my_insurance_contracts'),
                path('make_contract/', MakeContractPage.as_view(), name='make_contract'),
                path('insurance_objects/', ObjectsOfInsurancePage.as_view(), name='insurance_objects'),
                path('insurance_agents/', InsuranceAgentsPage.as_view(), name='insurance_agents'),
               ]
