from django.urls import path
from . import views

app_name = 'bank_system'

urlpatterns = [
    path("registerLoan/<int:app_id>/",
         views.register_loan, name="registerLoan"),
    path("bankLoans/", views.bank_loans, name="bankLoans"),
    path("declineLoan/<int:app_id>/", views.delete_loan, name="declineLoan"),
]
