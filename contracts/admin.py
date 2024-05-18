from django.contrib import admin

# Register your models here.
from .models import Contract, ContractStatus

@admin.register(ContractStatus)
class ContractStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_editable = ('is_active',)

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'company_name', 'status')
