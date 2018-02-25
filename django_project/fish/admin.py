# coding=utf-8

from django.contrib import admin
from fish.models import (
    FishCollectionRecord,
    IucnStatus,
    Taxon
)

admin.site.register(FishCollectionRecord)
admin.site.register(IucnStatus)
admin.site.register(Taxon)
