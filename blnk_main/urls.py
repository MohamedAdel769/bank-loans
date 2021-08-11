from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("application/<int:loan_id>/", views.add_application, name="application"),
]
