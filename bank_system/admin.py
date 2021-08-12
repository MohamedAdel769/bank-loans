from bank_system.models import Bank
from django.contrib import admin
from .models import *

admin.site.register(Bank)
admin.site.register(Bank_loan)
