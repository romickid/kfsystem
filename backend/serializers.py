from rest_framework import serializers
from .models import Admin, CustomerService, ChattingLog, SerialNumber, LANGUAGE_CHOICES, STYLE_CHOICES

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerService
        fields = ('id', 'email', 'nickname', 'password')

    def create(self, validated_data):
        return Admin.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance


class CustomerServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerService
        fields = ('id', 'email', 'nickname', 'password', 'is_online', 'connection_num')

    def create(self, validated_data):
        return CustomerService.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.password = validated_data.get('password', instance.password)
        instance.is_online = validated_data.get('is_online', instance.is_online)
        instance.connection_num = validated_data.get('connection_num', instance.connection_num)
        instance.save()
        return instance


class ChattingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model =ChattingLog
        fields=('id', 'client_id', 'service_id', 'content', 'is_client', 'time')

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


class SerialNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerialNumber
        fields = ('id', 'serials', 'is_used')

    def create(self, validated_data):
        return SerialNumber.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.serials = validated_data.get('serials', instance.serials)
        instance.is_used = validated_data.get('is_used', instance.is_used)
        instance.save()
        return instance
