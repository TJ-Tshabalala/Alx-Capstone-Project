from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Employee
from .serializers import EmployeeSerializer
from django.utils import timezone
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status


# Create your views here.

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def create(self, request, *args, **kwargs):
        user_data = request.data.pop('user')
        try:
            user = User.objects.create_user(**user_data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        employee_data = request.data
        employee_data['user'] = user.id
        serializer = self.get_serializer(data=employee_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        serializer.save()


class EmployeeRetrieveIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classess = [permissions.IsAuthenticatedOrReadOnly]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        user_data = request.data.pop('user', None)
        if user_data:
            user_serializer = UserSerializer(instance.user, data=user_data, partial=True)
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
        instance = self.get.object()

class UpcomingHires(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        now = timezone.now().date()
        return Employee.objects.filter(hire_date__gte=now).order_by('hire_date')
