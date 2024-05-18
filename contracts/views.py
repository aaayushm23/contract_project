# Create your views here.
from django.shortcuts import render, redirect
from .models import Contract
from .forms import ContractForm

def contract_list(request):
    contracts = Contract.objects.all()
    return render(request, 'contracts/contract_list.html', {'contracts': contracts})

def add_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contract_list')
    else:
        form = ContractForm()
    return render(request, 'contracts/contract_form.html', {'form': form})

def edit_contract(request, pk):
    contract = Contract.objects.get(pk=pk)
    if request.method == 'POST':
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contract_list')
    else:
        form = ContractForm(instance=contract)
    return render(request, 'contracts/contract_form.html', {'form': form})
