from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from . models import employees

class employee_serializer(serializers.ModelSerializer):
    class Meta:
        model=employees
        #fields=('firstname','lastname')
        fields='__all__'