from rest_framework import serializers
from .models import Company, NewEmployee, Device, Employee
from datetime import datetime

class CompanySerialiser(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"
    
class EmployeeSerialiser(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields="__all__"
        
class NewEmployeeSerialiser(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = NewEmployee
        fields="__all__"

class DeviceSerialiser(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Device
        fields="__all__"
        
# class AttandanceSerialiser(serializers.HyperlinkedModelSerializer):
#     id = serializers.ReadOnlyField()
#     class Meta:
#         model = Attandance
#         fields="__all__"