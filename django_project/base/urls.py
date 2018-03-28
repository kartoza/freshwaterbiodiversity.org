# coding=utf-8

from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from base.views.landing_page import LandingPageView
from base.api_views.location_site import (
    LocationSiteList,
    LocationSiteDetail,
)
from base.api_views.taxon import TaxonDetail
from base.views.csv_upload import CsvUploadView


api_urls = [
    url(r'^api/location-site/$', LocationSiteList.as_view()),
    url(r'^api/location-site/(?P<pk>[0-9]+)/$',
        LocationSiteDetail.as_view()),
    url(r'^api/taxon/(?P<pk>[0-9]+)/$',
        TaxonDetail.as_view()),
]

urlpatterns = [
    path('', TemplateView.as_view(template_name="landing_page.html")),
    path('map', LandingPageView.as_view()),
    url(r'^api/docs/', include_docs_urls(title='Healthyrivers API')),
    url(regex=r'^csv_uploader/$',
        view=CsvUploadView.as_view(),
        name='csv-upload'),
] + api_urls
