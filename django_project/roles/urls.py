# coding=utf-8
__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '21/02/18'

from django.conf.urls import url
from roles.tests.role import (
    test_role_access_1,
    test_role_access_2,
    test_permission_access_1,
    test_permission_access_2,
    test_permission_access_3,
)

urlpatterns_test = [
    url(r'^test/test_role_access_1/$', test_role_access_1),
    url(r'^test/test_role_access_2/$', test_role_access_2),
    url(r'^test/test_permission_access_1/$', test_permission_access_1),
    url(r'^test/test_permission_access_2/$', test_permission_access_2),
    url(r'^test/test_permission_access_3/$', test_permission_access_3),
]

urlpatterns = [] + urlpatterns_test
