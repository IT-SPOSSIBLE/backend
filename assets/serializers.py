from rest_framework import serializers
from .models import Assets
from api.serializers import UserTBSerializer
from contract.serializers import ContractSerializer
from django.contrib.auth import get_user_model

User= get_user_model

class AssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assets
        fields = ['id', 'contract', 'name', 'plate_number', 'description', 'status', 'created_at']

    def create(self, validated_data):

        request=self.context.get('request')

        if not request or not request.user.is_authenticated:

            raise serializers.ValidationError({"error": "User must be authenticated."})
        
        validated_data['boss']=request.user
        return super().create(validated_data)
