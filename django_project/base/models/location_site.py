# coding=utf-8
"""Site model definition.

"""

from django.core.exceptions import ValidationError
from django.contrib.gis.db import models
from base.models.location_type import LocationType


class LocationSite(models.Model):
    """Location Site model."""

    name = models.CharField(
        max_length=100,
        blank=False,
    )
    location_type = models.ForeignKey(
        LocationType,
        models.CASCADE,
        null=False,
    )
    geometry_point = models.PointField(
        null=True,
        blank=True,
    )
    geometry_line = models.LineStringField(
        null=True,
        blank=True,
    )
    geometry_polygon = models.PolygonField(
        null=True,
        blank=True,
    )
    geometry_multipolygon = models.MultiPolygonField(
        null=True,
        blank=True,
    )

    # noinspection PyClassicStyleClass
    class Meta:
        """Meta class for project."""
        app_label = 'base'

    def __str__(self):
        return u'%s' % self.name

    def save(self, *args, **kwargs):
        """Check if one of geometry is not null."""
        if self.geometry_point or self.geometry_line or \
                self.geometry_polygon or self.geometry_multipolygon:
            super(LocationSite, self).save(*args, **kwargs)
        else:
            raise ValidationError('At least one geometry need to be filled.')
