# coding=utf-8

from django.contrib import admin
from fish.models import (
    FishCollectionRecord,
    IUCNStatus,
    Taxon,
    CSVDocument
)


class IUCNStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'sensitive')


class TaxonAdmin(admin.ModelAdmin):
    list_display = ('common_name', 'author', 'iucn_status')


admin.site.register(FishCollectionRecord)
admin.site.register(IUCNStatus, IUCNStatusAdmin)
admin.site.register(Taxon, TaxonAdmin)
admin.site.register(CSVDocument)
