# coding=utf-8
"""Fish collection record model definition.

"""

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.dispatch import receiver

from base.models.location_site import LocationSite
from base.utils.gbif import update_fish_collection_record
from fish.models.taxon import Taxon


class FishCollectionRecord(models.Model):
    """First collection model."""
    HABITAT_CHOICES = (
        ('euryhaline', 'Euryhaline'),
        ('freshwater', 'Freshwater'),
    )
    CATEGORY_CHOICES = (
        ('alien', 'Alien'),
        ('indigenous', 'Indigenous'),
        ('translocated', 'Translocated')
    )
    site = models.ForeignKey(
        LocationSite,
        models.CASCADE,
    )
    original_species_name = models.CharField(
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
        default=True,
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
    taxon_gbif_id = models.ForeignKey(
        Taxon,
        models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Taxon GBIF ',
    )

    # noinspection PyClassicStyleClass
    class Meta:
        """Meta class for project."""
        app_label = 'fish'


@receiver(models.signals.post_save, sender=FishCollectionRecord)
def fish_collection_post_save_handler(sender, instance, **kwargs):
    """
    Fetch taxon from original species name.
    """
    models.signals.post_save.disconnect(
            fish_collection_post_save_handler,
            sender=sender
    )
    update_fish_collection_record(instance)
    models.signals.post_save.connect(
            fish_collection_post_save_handler,
            sender=sender
    )
