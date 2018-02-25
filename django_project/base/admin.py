# coding=utf-8

from django.contrib.gis import admin
from base.models import (
    LocationType,
    LocationSite,
)

admin.site.register(LocationSite)
admin.site.register(LocationType)
