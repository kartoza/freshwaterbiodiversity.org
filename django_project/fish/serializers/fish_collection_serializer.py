from rest_framework import serializers
from fish.models import FishCollectionRecord


class FishCollectionSerializer(serializers.ModelSerializer):
    """
    Serializer for fish collection model.
    """
    class Meta:
        model = FishCollectionRecord
        fields = '__all__'
