from rest_framework import serializers
from .models import Admin, CustomerService, LANGUAGE_CHOICES, STYLE_CHOICES,ChattingLog, SerialNumber

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
        fields = ('id', 'email', 'nickname', 'password')

    def create(self, validated_data):
        return CustomerService.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance


class ChattingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model =ChattingLog
        fields=('id','client_id','service_id','content','is_client','time')


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
