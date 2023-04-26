from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField()
