from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Customer, Loan, Loan_app
from bank_system.models import Bank_loan
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm, LoanAppForm
from django.core.exceptions import PermissionDenied


def display_message(request, message, extra_tags='', redirectRoute=None):
    messages.info(request, message, extra_tags=extra_tags)
    if redirectRoute is not None:
        return redirect(redirectRoute)


@login_required
def index(request):
    if request.user.groups.filter(name='bankers').exists():
        return redirect('blnk_main:banker_home')

    context = {
        'loans': Loan.objects.all(),
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
            return display_message(
                request, "You already have an active loan.", 'danger', 'blnk_main:index')

        form = LoanAppForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')

            Loan_app.objects.create(
                user=current_user, loan=selected_loan, amount=amount)

            messages.success(
                request, f'Loan Application Submitted for {current_user.username}')
            return redirect('blnk_main:index')
    else:
        form = LoanAppForm()

    context = {
        'loan': selected_loan,
        'form': form
    }

    return render(request, "blnk_main/application.html", context)


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

            messages.success(
                request, f'Profile updated for {current_user.username}')
            return redirect('blnk_main:index')
    else:
        form = CustomerForm()
    return render(request, 'blnk_main/customer.html', {'form': form})


@login_required
def app_info(request):
    current_user = request.user
    if current_user.groups.filter(name='bankers').exists():
        raise PermissionDenied

    status = False
    try:
        app = Loan_app.objects.get(user=current_user)
    except:
        app = current_user.customer.active_loans.first()
        if not app:
            messages.warning(
                request, 'You do not have any applications yet.')
            return redirect('blnk_main:index')
        status = True

    context = {
        'loan': app.loan,
        'app': app,
        'status': status
    }
    return render(request, 'blnk_main/my_app.html', context)
