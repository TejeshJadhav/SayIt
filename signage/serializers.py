from rest_framework import serializers


class SlideSerializer(serializers.Serializer):
    image = serializers.ImageField()
    duration = serializers.IntegerField()


class VideoSerializer(serializers.Serializer):
    url = serializers.URLField()
