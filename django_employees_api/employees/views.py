from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from rest_framework.permissions import IsAuthenticated
from .serializers import EmployeeSerializer


# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated] # Requires Authentication