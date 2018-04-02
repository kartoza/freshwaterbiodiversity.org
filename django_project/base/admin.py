# coding=utf-8

from django.contrib.gis import admin
from base.models import (
    LocationType,
    LocationSite,
    CSVDocument,
    IUCNStatus,
    Taxon,
    Survey,
    LocationContext,
)


class LocationSiteAdmin(admin.GeoModelAdmin):
    default_zoom = 5
    default_lat = -30
    default_lon = 25


class IUCNStatusAdmin(admin.ModelAdmin):
    list_display = ('get_category_display', 'sensitive')


class TaxonAdmin(admin.ModelAdmin):
    list_display = ('common_name', 'author', 'iucn_status')


admin.site.register(LocationSite, LocationSiteAdmin)
admin.site.register(LocationType)
admin.site.register(CSVDocument)
admin.site.register(IUCNStatus, IUCNStatusAdmin)
admin.site.register(Taxon, TaxonAdmin)
admin.site.register(Survey)
admin.site.register(LocationContext)
