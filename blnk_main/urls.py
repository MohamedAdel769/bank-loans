from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("application/<int:loan_id>/", views.add_application, name="application"),
    path("customer/", views.customer_info, name="customer"),
    path("myApplication/", views.app_info, name="myApplication"),
    path("banker_home/", views.banker_home, name="banker_home")
]
