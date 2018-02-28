# coding=utf-8

from django.contrib.gis import admin
from base.models import (
    LocationType,
    LocationSite,
    LocationTypeAllowedGeometry,
)
from base.forms.location_type import LocationTypeForm


class LocationSiteAdmin(admin.GeoModelAdmin):
    default_zoom = 5
    default_lat = -30
    default_lon = 25


class LocationTypeAdmin(admin.ModelAdmin):
    form = LocationTypeForm


admin.site.register(LocationSite, LocationSiteAdmin)
admin.site.register(LocationType)
admin.site.register(LocationTypeAllowedGeometry)
