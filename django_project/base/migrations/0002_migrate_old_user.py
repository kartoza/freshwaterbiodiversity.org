# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '06/03/17'

from django.db import connection, migrations
from django.db.utils import ProgrammingError

user_fields = ['username', 'firstname', 'surname', 'email']


def get_old_users():
    cursor = connection.cursor()
    cursor.execute('SELECT %s FROM "User"' % ','.join(user_fields))
    row = cursor.fetchall()
    return row


def import_data(apps, schema_editor):
    User = apps.get_model("base", "User")
    rows = []
    try:
        rows = get_old_users()
    except ProgrammingError:
        pass
    for row in rows:
        row_dictionary = {}
        for i, item in enumerate(user_fields):
            key = item
            row_dictionary[key] = row[i]

        user, created = User.objects.get_or_create(
            username=row_dictionary['username']
        )
        if created:
            user.first_name = row_dictionary['firstname']
            user.last_name = row_dictionary['surname']
            if row_dictionary['email']:
                user.email = row_dictionary['email']
            user.save()


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_data),
    ]
