from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import DashboardStat, Transaction
from django.contrib import messages

def index(request):
    stats = DashboardStat.objects.latest('created_at')
    transactions = Transaction.objects.order_by('-created_at')[:10]

    context = {
        'users': stats.users,
        'revenue': stats.revenue,
        'errors': stats.errors,
        'session': stats.session,
        'transactions': transactions
    }
    return render(request, 'main/index.html', context)

def add_transaction(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            amount = request.POST.get('amount')
            status = request.POST.get('status')
            
            Transaction.objects.create(
                name=name,
                amount=amount,
                status=status
            )
            
            messages.success(request, 'Transaction added successfully!')
        except Exception as e:
            messages.error(request, f'Error adding transaction: {str(e)}')
        
        return redirect('index')
    
    # If not POST, redirect to index
    return redirect('index')

def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    
    if request.method == 'POST':
        try:
            transaction.name = request.POST.get('name')
            transaction.amount = request.POST.get('amount')
            transaction.status = request.POST.get('status')
            transaction.save()
            
            messages.success(request, 'Transaction updated successfully!')
        except Exception as e:
            messages.error(request, f'Error updating transaction: {str(e)}')
        
        return redirect('index')
    
    # If not POST, redirect to index
    return redirect('index')

def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    
    if request.method == 'POST':
        try:
            transaction.delete()
            messages.success(request, 'Transaction deleted successfully!')
        except Exception as e:
            messages.error(request, f'Error deleting transaction: {str(e)}')
        
        return redirect('index')
    
    # If not POST, redirect to index
    return redirect('index')