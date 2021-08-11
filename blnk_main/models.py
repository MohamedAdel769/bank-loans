from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active_loan = models.BooleanField(default=False)
    company_name = models.CharField(max_length=15, null=True)
    salary = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.salary}"


class Loan(models.Model):
    min_val = models.IntegerField()
    max_val = models.IntegerField()
    interest_rate = models.FloatField()
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.min_val} - {self.max_val}, {self.interest_rate}"


class Loan_app(models.Model):
    types = (('Fund', 'Fund'), ('Loan', 'Loan'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    app_type = models.CharField(max_length=10, choices=types)
    amount = models.IntegerField()
    status = models.BooleanField(default=False)
    loan_term = models.IntegerField()


class Banker(models.Model):
    total_loans = models.IntegerField()
    total_funds = models.IntegerField()
