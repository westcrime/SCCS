from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class InsuranceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'content', 'ins_coef', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class ObjectOfInsuranceAdmin(admin.ModelAdmin):
    list_display = ('insured_risks', 'cost', 'ins_cat')
    search_fields = ('insured_risks', 'cost')


class InsuranceAgentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'surname', 'address', 'phone_number', 'total_earning', 'slug')
    search_fields = ('first_name', 'last_name', 'surname', 'total_earning', 'address', 'phone_number')
    list_filter = ('first_name', 'last_name', 'total_earning')
    prepopulated_fields = {"slug": ("first_name",)}


class InsuranceBranchAdmin(admin.ModelAdmin): #Филиал страхования
    list_display = ('name', 'address', 'phone_number', 'tariff_rate')
    search_fields = ('name', 'address', 'phone_number', 'tariff_rate')
    list_filter = ('name', 'tariff_rate')


class InsuranceContractAdmin(admin.ModelAdmin):
    list_display = ('ins_object', 'time_create', 'time_end', 'ins_agent', 'ins_client', 'total_cost')
    search_fields = ('ins_object', 'time_create', 'time_end', 'ins_agent', 'ins_client', 'total_cost')
    list_filter = ('time_create', 'time_end', 'total_cost')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number')


admin.site.register(User, UserAdmin)
admin.site.register(InsuranceCategory, InsuranceCategoryAdmin)
admin.site.register(InsuranceAgent, InsuranceAgentAdmin)
admin.site.register(InsuranceBranch, InsuranceBranchAdmin)
admin.site.register(InsuranceContract, InsuranceContractAdmin)
admin.site.register(ObjectOfInsurance, ObjectOfInsuranceAdmin)
