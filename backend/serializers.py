from rest_framework import serializers
from .models import Admin, CustomerService, ChattingLog, SerialNumber, ImageLog, LANGUAGE_CHOICES, STYLE_CHOICES


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('id', 'email', 'nickname', 'password', 'web_url', 'widget_url', 'mobile_url', 'communication_key', 'vid')

    def create(self, validated_data):
        return Admin.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.password = validated_data.get('password', instance.password)
        instance.web_url = validated_data.get('web_url', instance.web_url)
        instance.widget_url = validated_data.get('widget_url', instance.widget_url)
        instance.mobile_url = validated_data.get('mobile_url', instance.mobile_url)
        instance.communication_key = validated_data.get('communication_key', instance.communication_key)
        instance.vid = validated_data.get('vid', instance.vid)
        instance.save()
        return instance


class CustomerServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerService
        fields = ('id', 'email', 'nickname', 'password', 'is_online', 'connection_num', 'vid')

    def create(self, validated_data):
        return CustomerService.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.password = validated_data.get('password', instance.password)
        instance.is_online = validated_data.get('is_online', instance.is_online)
        instance.connection_num = validated_data.get('connection_num', instance.connection_num)
        instance.vid = validated_data.get('vid', instance.vid)
        instance.save()
        return instance


class ChattingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChattingLog
        fields = ('id', 'client_id', 'service_id', 'content', 'is_client', 'time')

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

class ImageLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageLog
        fields = ('id', 'client_id', 'service_id', 'content', 'is_client', 'time')

    def create(self, validated_data):
        return ImageLog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.client_id = validated_data.get('client_id', instance.client_id)
        instance.service_id = validated_data.get('service_id', instance.service_id)
        instance.image = validated_data.get('image', instance.image)
        instance.is_client = validated_data.get('is_client', instance.is_client)
        instance.time = validated_data.get('time', instance.time)
        instance.save()
        return instance
