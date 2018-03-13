# coding=utf-8

from django.conf.urls import url
from fish.views.csv_upload import CsvUploadView
from fish.api_views.fish_collection_record import FishCollectionList

urlpatterns = [
    url(regex=r'^csv_uploader/$',
        view=CsvUploadView.as_view(),
        name='csv-upload'),
    url(r'^fish-collections/$', FishCollectionList.as_view()),
]
