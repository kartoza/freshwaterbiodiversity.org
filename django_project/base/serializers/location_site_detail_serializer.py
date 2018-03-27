from base.models.location_site import LocationSite
from base.serializers.location_site_serializer import LocationSiteSerializer
from fish.serializers.fish_collection_serializer import \
    FishCollectionSerializer


class LocationSiteDetailSerializer(LocationSiteSerializer):
    """
    Serializer for location site detail.
    """
    fish_collection_records = FishCollectionSerializer(many=True)

    class Meta:
        model = LocationSite
        fields = [
            'id',
            'geometry',
            'location_type',
            'fish_collection_records']
