from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # ('id', 'name', 'email', 'mobile_number', 'latitude', 'longitude', 'address')

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer()

    class Meta:
        model = Task
        fields = ('id', 'name', 'date_time', 'assigned_to', 'status')
