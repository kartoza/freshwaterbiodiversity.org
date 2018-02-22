# coding=utf-8
__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '21/02/18'

from django.contrib.auth.admin import UserAdmin
from django.contrib.gis import admin
from django.contrib.auth.models import User, Group
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from rolepermissions.admin import RolePermissionsUserAdminMixin

admin.site.unregister(User)
admin.site.unregister(Group)


class RolePermissionsUserAdmin(RolePermissionsUserAdminMixin, UserAdmin):
    """ Displaying user using rolepermission library.
    Hide permissions because it will be
    automatically assign if groups is changed.

    """
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff', 'roles')
    readonly_fields = ('role_permissions',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'first_name', 'last_name', 'email')}),
        (_('Roles'), {'fields': ('groups', 'role_permissions')}),
        (_('Permissions'), {'fields': (
            'is_active', 'is_staff', 'is_superuser'
        )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    def roles(self, obj):
        roles = []
        for group in obj.groups.all():
            roles.append(group.name)
        return ','.join(roles)

    def role_permissions(self, obj):
        permissions = []
        for permission in obj.user_permissions.all():
            permissions.append(
                '- %s' % permission.name.replace('auth | user | ', '')
            )
        return format_html('<br>'.join(permissions))

    role_permissions.allow_tags = True


admin.site.register(User, RolePermissionsUserAdmin)
