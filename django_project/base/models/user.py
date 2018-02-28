__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '26/02/18'

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        ordering = ('first_name',)
        app_label = 'base'

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
