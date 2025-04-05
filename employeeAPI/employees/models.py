from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#User model to hold employee fields
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    hire_Date = models.DateField()

    def __str__(self):
        return self.user.username
    