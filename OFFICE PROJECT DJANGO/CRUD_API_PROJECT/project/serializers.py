from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    stream=serializers.CharField(max_length=100)
    subject=serializers.CharField(max_length=50)
    join_at=serializers.DateTimeField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
