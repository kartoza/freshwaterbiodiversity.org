# noinspection PyUnresolvedReferences,PyPackageRequirements
import factory
import random
from base.models import LocationType, LocationSite
from django.contrib.gis.geos import Point


class LocationTypeF(factory.django.DjangoModelFactory):
    """
    Location type factory
    """
    class Meta:
        model = LocationType

    name = factory.Sequence(lambda n: 'Test location type %s' % n)
    description = u'Only for testing'


class LocationSiteF(factory.django.DjangoModelFactory):
    """
    Location site factory
    """
    class Meta:
        model = LocationSite

    location_type = factory.SubFactory(LocationTypeF)
    geometry_point = Point(
        random.uniform(-180.0, 180.0),
        random.uniform(-90.0, 90.0)
    )
