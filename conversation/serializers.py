from rest_framework import serializers

from .models import Conversation

class ConversationSerializer(serializers.Serializer):
    class Meta:
        model=Conversation
        fields='__all__'


    def create(self,validated_data):
        conversation=Conversation.objects.create(**validated_data)
        return conversation