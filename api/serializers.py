from rest_framework import serializers
from .models import Person
import re

class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = ["id", "name"]

    def validate_name(self, name):
        if not re.search('[a-zA-Z]', name):
            raise serializers.ValidationError("Name must be s string.")
        return name
      

    