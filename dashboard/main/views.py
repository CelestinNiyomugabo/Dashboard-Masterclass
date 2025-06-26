from django.shortcuts import render 
from django.http import HttpResponse
from .models import DashboardStat, Transaction 


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

def home(request):
    return HttpResponse("This is my home page")