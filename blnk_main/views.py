from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import serializers
from .models import Customer, Loan, Loan_app
from bank_system.models import Bank_loan
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm, LoanAppForm
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from .serializers import LoanSerializer
from django.urls import reverse


def display_message(request, message, extra_tags='', redirectRoute=None):
    messages.info(request, message, extra_tags=extra_tags)
    if redirectRoute is not None:
        return redirect(redirectRoute)


@login_required
def index(request):
    if request.user.groups.filter(name='bankers').exists():
        return redirect('blnk_main:banker_home')

    context = {
        'loans': Loan.objects.filter(loan_type='Loans'),
        'title': 'home'
    }
    return render(request, "blnk_main/index.html", context)


def banker_home(request):
    if not request.user.groups.filter(name='bankers').exists():
        raise PermissionDenied

    context = {
        'title': 'banker',
        'apps': Loan_app.objects.all()
    }
    return render(request, "blnk_main/banker_home.html", context)


@login_required
def add_application(request, loan_id):
    current_user = request.user
    if not Customer.objects.filter(user=current_user).exists():
        return redirect('blnk_main:customer')

    selected_loan = Loan.objects.get(id=loan_id)
    if request.method == 'POST':
        # check is customer has an application
        if Loan_app.objects.filter(user=current_user).exists():
            return display_message(
                request, "You already have an application.", 'danger', 'blnk_main:index')

        if Bank_loan.objects.filter(customer=current_user.customer).exists():
            bank_loans = Bank_loan.objects.filter(
                customer=current_user.customer)
            for bank_loan in bank_loans:
                if bank_loan.loan.loan_type == 'Loans':
                    return display_message(
                        request, "You already have an active loan.", 'danger', 'blnk_main:index')

        form = LoanAppForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')

            if amount < selected_loan.min_val or amount > selected_loan.max_val:
                display_message(
                    request, "Please enter a valid amount.", 'danger')
                return redirect(reverse('blnk_main:application', kwargs={'loan_id': loan_id}))

            Loan_app.objects.create(
                user=current_user, loan=selected_loan, amount=amount)

            return display_message(request, f'Loan Application Submitted for {current_user.username}', 'success', 'blnk_main:index')
    else:
        form = LoanAppForm()

    context = {
        'loan': selected_loan,
        'form': form
    }

    return render(request, "blnk_main/application.html", context)


@login_required
def customer_info(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data.get('first_name')
            l_name = form.cleaned_data.get('last_name')
            company = form.cleaned_data.get('company_name')
            salary = form.cleaned_data.get('salary')
            current_user = request.user
            User.objects.filter(id=current_user.id).update(
                first_name=f_name, last_name=l_name)

            Customer.objects.create(
                user=current_user, company_name=company, salary=salary)

            return display_message(request, f'Profile updated for {current_user.username}', 'success', 'blnk_main:index')

    else:
        form = CustomerForm()
    return render(request, 'blnk_main/customer.html', {'form': form})


@login_required
def app_info(request):
    current_user = request.user
    if current_user.groups.filter(name='bankers').exists():
        raise PermissionDenied

    try:
        app = Loan_app.objects.get(user=current_user)
    except:
        return display_message(request, 'You do not have any applications yet.', 'danger', 'blnk_main:index')

    context = {
        'loan': app.loan,
        'app': app,
        'status': False
    }
    return render(request, 'blnk_main/my_app.html', context)


@login_required
def active_apps(request):
    current_user = request.user
    try:
        app = current_user.customer.active_loans.first()
        if app is None:
            return display_message(request, 'You do not have any active applications yet.', 'danger', 'blnk_main:index')

    except:
        return display_message(request, 'You do not have any active applications yet.', 'danger', 'blnk_main:index')

    context = {
        'loan': app.loan,
        'app': app,
        'status': True
    }
    return render(request, 'blnk_main/my_app.html', context)


class filterPlans(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request, format=None):
        plan = request.data['plan']
        loans = Loan.objects.filter(loan_type=plan)
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)
