from rest_framework import serializers
from base.models.location_site import LocationSite
from base.serializers.location_type_serializer import LocationTypeSerializer


class LocationSiteSerializer(serializers.ModelSerializer):
    """
    Serializer for location site model.
    """
    geometry = serializers.SerializerMethodField()
    location_type = LocationTypeSerializer(read_only=True)

    def get_geometry(self, obj):
        geometry = obj.get_geometry()
        if geometry:
            return obj.get_geometry().json
        return ''

    class Meta:
        model = LocationSite
        fields = ['id', 'geometry', 'location_type']
