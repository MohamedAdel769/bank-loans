from django.urls import path, include
from . import views

app_name = 'blnk_main'

urlpatterns = [
    path("", views.index, name="index"),
    path("application/<int:loan_id>/", views.add_application, name="application"),
    path("customer/", views.customer_info, name="customer"),
    path("myApplication/", views.app_info, name="myApplication"),
    path("activeApplication", views.active_apps, name="activeApplication"),
    path("banker_home/", views.banker_home, name="banker_home"),
    path("filter_plans/", views.filterPlans.as_view(), name="filterPlans"),
]
