from rest_framework import serializers
from .models import Admin, CustomerService, ChattingLog, SerialNumber, BigImageLog, SmallImageLog, EnterpriseDisplayInfo, RobotInfo, LANGUAGE_CHOICES, STYLE_CHOICES
from drf_extra_fields.fields import Base64ImageField


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('id', 'email', 'nickname', 'password', 'web_url', 'widget_url', 'mobile_url', 'communication_key', 'vid', 'vid_createtime')


class CustomerServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerService
        fields = ('id', 'email', 'enterprise', 'nickname', 'password', 'is_register', 'is_online', 'connection_num', 'vid', 'vid_createtime')


class CustomerServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerService
        fields = ('id', 'email', 'nickname', 'password', 'is_register', 'is_online', 'connection_num', 'vid', 'vid_createtime')


class ChattingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChattingLog
        fields = ('id', 'client_id', 'service_id', 'content', 'is_client', 'time')


class SerialNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerialNumber
        fields = ('id', 'serials', 'is_used')


class BigImageLogSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    class Meta:
        model = BigImageLog
        fields = ('id', 'client_id', 'service_id', 'image', 'extention', 'is_client', 'time', 'label')


class SmallImageLogSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    class Meta:
        model = SmallImageLog
        fields = ('id', 'client_id', 'service_id', 'image', 'extention', 'is_client', 'time', 'label')


class EnterpriseDisplayInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterpriseDisplayInfo
        fields = ('id', 'enterprise', 'name', 'comment')


class RobotInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RobotInfo
        fields = ('id', 'enterprise', 'question', 'answer', 'keyword', 'weight')
