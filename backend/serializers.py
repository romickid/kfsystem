from rest_framework import serializers
from .models import Admin, CustomerService, LANGUAGE_CHOICES, STYLE_CHOICES,ChattingLog

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


class ChattingLogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    client_id=serializers.CharField(max_length=100,default='null')
    service_id=serializers.CharField()
    content=serializers.CharField(max_length=500,default='null')
    is_client=serializers.BooleanField(default=False)
    time=serializers.DateTimeField()

    def create(self, validated_data):
        return ChattingLog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.client_id = validated_data.get('client_id', instance.client_id)
        instance.service_id = validated_data.get('service_id', instance.service_id)
        instance.content = validated_data.get('content', instance.content)
        instance.is_client = validated_data.get('is_client', instance.is_client)
        instance.time = validated_data.get('time', instance.time)
        instance.save()
        return instance