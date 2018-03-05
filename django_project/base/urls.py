# coding=utf-8

from django.urls import path
from django.views.generic import TemplateView
from base.views.landing_page import LandingPageView

urlpatterns = [
    path('', TemplateView.as_view(template_name="landing_page.html")),
    path('map', LandingPageView.as_view()),
]
