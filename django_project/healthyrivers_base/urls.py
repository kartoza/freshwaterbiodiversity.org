# coding=utf-8
from django.conf.urls import url
from views.download_csv_taxa_records import download_csv_site_taxa_records

urlpatterns = [
    url(r'^download-csv-taxa-records/$',
        download_csv_site_taxa_records,
        name='fish-site-download'),
]
