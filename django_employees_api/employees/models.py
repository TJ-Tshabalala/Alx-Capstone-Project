from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#Create an Employee Model
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Associate with User
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hire_date= models.DateField()

    def __str__(self):
        return self.user.username
    
    
