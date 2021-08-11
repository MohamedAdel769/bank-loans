from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Loan
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    context = {
        'loans': Loan.objects.all(),
        'title': 'home'
    }
    return render(request, "blnk_main/index.html", context)


def add_application(request, loan_id):
    loan = Loan.objects.get(id=loan_id)
    return render(request, "blnk_main/application.html", {"loan": loan})
