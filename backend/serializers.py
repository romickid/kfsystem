from rest_framework import serializers
from .models import Admin, CustomerService, SerialNumber, LANGUAGE_CHOICES, STYLE_CHOICES

class AdminSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length = 200)
    nickname = serializers.CharField(max_length = 100, default = "null")
    password = serializers.CharField(max_length = 128, default = "null")

    def create(self, validated_data):
        return Admin.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

class CustomerServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length = 200)
    nickname = serializers.CharField(max_length = 100, default = "null")
    password = serializers.CharField(max_length = 128, default = "null")

    def create(self, validated_data):
        return CustomerService.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

class SerialNumberSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    serials = serializers.CharField(max_length = 200)
    is_used = serializers.BooleanField(default = False)

    def create(self, validated_data):
        return SerialNumber.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.serials = validated_data.get('serials', instance.serials)
        instance.is_used = validated_data.get('is_used', instance.is_used)
        instance.save()
        return instance