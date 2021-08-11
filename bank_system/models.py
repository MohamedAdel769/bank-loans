from django.db import models
from django.db.models.deletion import CASCADE
from blnk_main.models import Customer, Loan


class Bank(models.Model):
    name = models.CharField(max_length=15)
    total_loans = models.IntegerField()
    total_funds = models.IntegerField()


class Bank_loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    loan_info = models.ForeignKey(Loan, on_delete=models.RESTRICT)
    amount = models.IntegerField()
    bank = models.ForeignKey(Bank, on_delete=CASCADE, related_name='loans')
    # amort table
