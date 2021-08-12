from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from .models import Bank, Bank_loan
from blnk_main.models import Loan_app
from django.contrib import messages


def register_loan(request, app_id):
    if not request.user.groups.filter(name='bankers').exists():
        raise PermissionDenied

    app = Loan_app.objects.get(id=app_id)
    bank = Bank.objects.first()  # there is only one bank now
    # check bank balance if it is a LOAN

    LOAN_APP = True if app.loan.loan_type == 'Loans' else False
    if LOAN_APP:
        if not bank.check_balance(app.amount):
            messages.error(
                request, 'Error! There is not enough fund', extra_tags='danger')
            return redirect('blnk_main:banker_home')

    # update balance
    bank.update_balance(app.amount, LOAN_APP)
    bank.save()

    # create bank loan
    Bank_loan.objects.create(
        customer=app.user.customer,
        loan=app.loan,
        amount=app.amount,
        bank=bank,
    )
    messages.success(
        request, f'{app.loan.loan_type} Registered Successfully')

    # remove loan from loan apps
    Loan_app.objects.filter(id=app_id).delete()

    return redirect('blnk_main:banker_home')


def delete_loan(request, app_id):
    if not request.user.groups.filter(name='bankers').exists():
        raise PermissionDenied

    Loan_app.objects.filter(id=app_id).delete()

    messages.success(
        request, 'Loan Declined')

    return redirect('blnk_main:banker_home')


def bank_loans(request):
    if not request.user.groups.filter(name='bankers').exists():
        raise PermissionDenied
    # filter with banker --> bank
    bank = Bank.objects.first()
    active_loans = bank.loans.all()
    return render(request, "bank_system/active_loans.html", {'loans': active_loans})
