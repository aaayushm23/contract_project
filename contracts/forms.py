from django import forms
from .models import Contract, ContractStatus

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['name', 'start_date', 'end_date', 'description', 'company_name', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].queryset = ContractStatus.objects.filter(is_active=True)
