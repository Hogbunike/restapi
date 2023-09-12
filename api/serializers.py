from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Person
import re

class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = '__all__'

    def validate_name(self, name):
        if not re.search('[a-zA-Z]', name):
            raise serializers.ValidationError("Name must be a string.")
        return name

    