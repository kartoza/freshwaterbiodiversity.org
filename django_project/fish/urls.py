# coding=utf-8

from django.conf.urls import url
from fish.api_views.fish_collection_record import (
    FishCollectionList,
    FishCollectionDetail,
)


api_urls = [
    url(r'^api/fish-collections/$', FishCollectionList.as_view()),
    url(r'^api/fish-collections/(?P<pk>[0-9]+)/$',
        FishCollectionDetail.as_view()),
]

urlpatterns = [
] + api_urls
