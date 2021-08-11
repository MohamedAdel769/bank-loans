from django.db.models import fields
from rest_framework import serializers
from .models import Bank_loan


class Loan_serializer(serializers.ModelSerializer):
    class Meta:
        model = Bank_loan
        fields = '__all__'
