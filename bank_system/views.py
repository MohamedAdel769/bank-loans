from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import bankSerializer

@api_view(['POST'])
def add
