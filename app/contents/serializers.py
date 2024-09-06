from rest_framework import serializers
from contents.models import Request, RequestMessage

class RequestSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Request
        fields = ['id', 'user', 'title', 'content']
        
class RequestListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Request
        fields = ['id', 'user', 'title',]

class RequestMessageSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = RequestMessage
        fields = ['user', 'content']

class AddRequestMessageSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = RequestMessage
        fields = ['request', 'user', 'content']
