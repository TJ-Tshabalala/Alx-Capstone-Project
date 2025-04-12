from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password') # Include password for create

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ('id','user','department','position','hire_date')

    # Create User
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee
    #Update the user
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        if user_data.get('password'):
            user.set_password(user_data['password'])
        user.save()


        instance.department = validated_data.get('department', instance.department)
        instance.position = validated_data.get('position', instance.position)
        instance.hire_date = validated_data.get('hire_date', instance.hire_date)
        instance.save()


        return instance