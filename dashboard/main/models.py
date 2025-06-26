from django.db import models

# Create your models here.
class DashboardStat(models.Model):
    users = models.IntegerField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    errors = models.IntegerField()
    session = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)