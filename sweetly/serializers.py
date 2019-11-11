from rest_framework import serializers


class URLSerializer(serializers.Serializer):
    long_url = serializers.URLField(max_length=1000,
                                    min_length=None,
                                    allow_blank=True)
