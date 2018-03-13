# coding=utf-8

from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from base.views.landing_page import LandingPageView

urlpatterns = [
    path('', TemplateView.as_view(template_name="landing_page.html")),
    path('map', LandingPageView.as_view()),
    url(r'^api/docs/', include_docs_urls(title='Healthyrivers API'))
]
