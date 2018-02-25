# coding=utf-8
"""Fish collection record model definition.

"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from base.models.location_site import LocationSite


class FishCollectionRecord(models.Model):
    """First collection model."""
    HABITAT_CHOICES = (
        ('euryhaline', 'Euryhaline'),
        ('freshwater', 'Freshwater'),
    )
    CATEGORY_CHOICES = (
        ('alien', 'Alien'),
        ('indigenouse', 'Indigenous'),
        ('translocated', 'Translocated')
    )

    site = models.ForeignKey(
        LocationSite,
        models.CASCADE,
    )
    locality_id = models.IntegerField(
        blank=True,
        null=True,
    )
    species = models.CharField(
        max_length=100,
        blank=True,
        default='',
    )
    habitat = models.CharField(
        max_length=50,
        choices=HABITAT_CHOICES,
        blank=True,
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        blank=True,
    )
    present = models.BooleanField(
        default=False,
    )
    collection_date = models.DateField(
        default=timezone.now
    )
    collector = models.CharField(
        max_length=100,
        blank=True,
        default='',
    )
    owner = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    notes = models.TextField(
        blank=True,
        default='',
    )