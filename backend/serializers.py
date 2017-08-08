from rest_framework import serializers
from .models import Admin, CustomerService, ChattingLog, SerialNumber, ImageLog, LANGUAGE_CHOICES, STYLE_CHOICES


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('id', 'email', 'nickname', 'password', 'web_url', 'widget_url', 'mobile_url', 'communication_key', 'vid')


class CustomerServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerService
        fields = ('id', 'email', 'enterprise', 'nickname', 'password', 'is_register', 'is_online', 'connection_num', 'vid')


class CustomerServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerService
        fields = ('id', 'email', 'nickname', 'password', 'is_register', 'is_online', 'connection_num', 'vid')


class ChattingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChattingLog
        fields = ('id', 'client_id', 'service_id', 'content', 'is_client', 'time')


class SerialNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerialNumber
        fields = ('id', 'serials', 'is_used')


class ImageLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageLog
        fields = ('id', 'client_id', 'service_id', 'content', 'is_client', 'time')
