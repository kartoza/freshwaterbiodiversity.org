# coding=utf-8
"""Location type definition.

"""

from django.db import models


class LocationTypeAllowedGeometry(models.Model):
    """Location type allowed geometry model."""

    GEOMETRY_CHOICES = (
        ('POINT', 'Point'),
        ('LINE', 'Line'),
        ('POLYGON', 'Polygon'),
        ('MULTIPOLYGON', 'Multipolygon'),
    )
    allowed_geometry = models.CharField(
        max_length=20,
        choices=GEOMETRY_CHOICES,
        unique=True
    )

    def __str__(self):
        return self.allowed_geometry


class LocationType(models.Model):
    """Location type model."""

    name = models.CharField(
        max_length=100,
        blank=False,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    allowed_geometry = models.ManyToManyField(LocationTypeAllowedGeometry)

    # noinspection PyClassicStyleClass
    class Meta:
        """Meta class for project."""
        app_label = 'base'
        ordering = ['name']

    def __str__(self):
        return u'%s' % self.name
