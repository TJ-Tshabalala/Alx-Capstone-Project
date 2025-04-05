from django.urls import path
from .views import EmployeeListCreate, EmployeeRetrieveUpdateDestroy, UpcomingHires

urlpatterns = [
    path('employees/', EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroy.as_view(), name='employee-retrieve-update-destroy'),
    path('upcoming_hires/', UpcomingHires.as_view(), name= 'upcoming-hires'),
]