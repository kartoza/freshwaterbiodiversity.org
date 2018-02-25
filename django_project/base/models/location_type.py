# coding=utf-8
"""Location type definition.

"""

from django.db import models


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

    def __unicode__(self):
        return u'%s' % self.name
