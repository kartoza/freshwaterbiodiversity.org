# coding=utf-8
"""Site model definition.

"""

from django.contrib.gis.db import models
from base.models.location_type import LocationType


class LocationSite(models.Model):
    """Location Site model."""

    location_type = models.ForeignKey(
        LocationType,
        models.SET_NULL,
        null=True,
    )
    geometry = models.PointField()

    # noinspection PyClassicStyleClass
    class Meta:
        """Meta class for project."""
        app_label = 'base'

    def __unicode__(self):
        return u'%s' % self.location_type.name
