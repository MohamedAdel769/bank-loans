from django.db import models
from django.db.models.deletion import CASCADE
from blnk_main.models import Customer, Loan


class Bank(models.Model):
    name = models.CharField(max_length=15)
    total_loans = models.IntegerField()
    total_funds = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}"

    def check_balance(self, amount):
        if self.total_loans + amount > self.total_funds:
            return False
        return True

    def update_balance(self, amount, loan_flag):
        if loan_flag:
            self.total_loans += amount
        else:
            self.total_funds += amount


class Bank_loan(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.RESTRICT, related_name='active_loans')
    loan = models.ForeignKey(Loan, on_delete=models.RESTRICT)
    amount = models.IntegerField()
    bank = models.ForeignKey(Bank, on_delete=CASCADE, related_name='loans')
    # amort table

    def __str__(self) -> str:
        return f'{self.bank.name} - {self.amount} EGP'
