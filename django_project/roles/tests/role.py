# coding=utf-8
__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '21/02/18'

from django.http import HttpResponse
from django.test import TestCase, Client
from django.contrib.auth.models import User

from rolepermissions.roles import AbstractUserRole
from rolepermissions.decorators import (
    has_role_decorator, has_permission_decorator
)


class TestRole1(AbstractUserRole):
    role_name = 'test_role'
    available_permissions = {
        'test_role_permission_1': True
    }


class TestRole2(AbstractUserRole):
    role_name = 'test_role_2'
    available_permissions = {
        'test_role_permission_2': True,
        'test_role_permission_3': True
    }


@has_role_decorator(TestRole1.role_name)
def test_role_access_1(request, *args, **kwargs):
    return HttpResponse('')


@has_role_decorator(TestRole2.role_name)
def test_role_access_2(request, *args, **kwargs):
    return HttpResponse('')


@has_permission_decorator(list(TestRole1.available_permissions.keys())[0])
def test_permission_access_1(request, *args, **kwargs):
    return HttpResponse('')


@has_permission_decorator(list(TestRole2.available_permissions.keys())[0])
def test_permission_access_2(request, *args, **kwargs):
    return HttpResponse('')


@has_permission_decorator(list(TestRole2.available_permissions.keys())[1])
def test_permission_access_3(request, *args, **kwargs):
    return HttpResponse('')


class UserRoleTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='username',
            password='password'
        )
        self.client = Client()
        self.client.login(username='username', password='password')

    def test_user_role_access(self):
        """
        Test user to access test_role_access.
        1. test user doesn't assigned to Role 1
        2. test assigned to Role 1
        3. test user to access role access 2
        4. assing to role access 2 and access the view
        """
        request = self.client.get(
            "/roles/test/test_role_access_1/", follow=True)
        self.assertEqual(request.status_code, 403)

        # assign role 1
        TestRole1.assign_role_to_user(self.user)

        request = self.client.get(
            "/roles/test/test_role_access_1/", follow=True)
        self.assertEqual(request.status_code, 200)

        # test role 2 is forbidden
        request = self.client.get(
            "/roles/test/test_role_access_2/", follow=True)
        self.assertEqual(request.status_code, 403)

        # assign role 2
        TestRole2.assign_role_to_user(self.user)

        request = self.client.get(
            "/roles/test/test_role_access_2/", follow=True)
        self.assertEqual(request.status_code, 200)

    def test_user_permission_by_role_access(self):
        """
        Test user to access test_permission with using role.
        """
        request = self.client.get(
            "/roles/test/test_permission_access_1/", follow=True)
        self.assertEqual(request.status_code, 403)

        # assign role 1
        # role 1 has permission for permission 1
        TestRole1.assign_role_to_user(self.user)

        request = self.client.get(
            "/roles/test/test_permission_access_1/", follow=True)
        self.assertEqual(request.status_code, 200)

        request = self.client.get(
            "/roles/test/test_permission_access_2/", follow=True)
        self.assertEqual(request.status_code, 403)

        request = self.client.get(
            "/roles/test/test_permission_access_3/", follow=True)
        self.assertEqual(request.status_code, 403)

        # assign role 2 and remove role 1
        # role 2 has permission for permission 2 & 3
        TestRole1.remove_role_from_user(self.user)
        TestRole2.assign_role_to_user(self.user)

        request = self.client.get(
            "/roles/test/test_permission_access_1/", follow=True)
        self.assertEqual(request.status_code, 403)

        request = self.client.get(
            "/roles/test/test_permission_access_2/", follow=True)
        self.assertEqual(request.status_code, 200)

        request = self.client.get(
            "/roles/test/test_permission_access_3/", follow=True)
        self.assertEqual(request.status_code, 200)
