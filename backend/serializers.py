from rest_framework import serializers
from .models import Snippet, Admin, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('title', instance.title)
        return instance


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