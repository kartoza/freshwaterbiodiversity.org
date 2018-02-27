# coding=utf-8
"""Csv document model definition.

"""

import os
from django.db import models
from django.dispatch import receiver


class CsvDocument(models.Model):
    """Csv document model
    """
    csv_file = models.FileField(upload_to='csv/')

    # noinspection PyClassicStyleClass
    class Meta:
        """Meta class for project."""
        app_label = 'fish'


@receiver(models.signals.post_delete, sender=CsvDocument)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.csv_file:
        if os.path.isfile(instance.csv_file.path):
            os.remove(instance.csv_file.path)
