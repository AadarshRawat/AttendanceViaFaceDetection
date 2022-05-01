from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    rollnumber=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    lname=serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.rollnumber=validated_data.get('rollnumber',instance.rollnumber)
        instance.name=validated_data.get('name',instance.name)
        instance.lname=validated_data.get('lname',instance.lname)
        instance.save()
        return instance
    
        