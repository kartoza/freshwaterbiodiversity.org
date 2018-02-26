# coding=utf-8

from django.conf.urls import url
from fish.views.csv_upload import CsvUploadView

urlpatterns = [
    url(regex=r'^csv_uploader/$',
        view=CsvUploadView.as_view(),
        name='csv-upload'),
]
