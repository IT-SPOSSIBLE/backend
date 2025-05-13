from rest_framework import serializers

from .models import MotocycleImage


class MotocycleSerializer(serializers.Serializer):
    class Meta:
        model=MotocycleImage
        fields='__all__'



    def create(self,validated_data):
        motocycleImage=MotocycleImage.objects.create(**validated_data)
        return motocycleImage