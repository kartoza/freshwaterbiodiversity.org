__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '26/02/18'

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualifications = models.CharField(
        max_length=250,
        blank=True,
        default=''
    )
    other = models.CharField(
        max_length=100,
        blank=True,
        default=''
    )

    class Meta:
        ordering = ('user__first_name',)
        app_label = 'profile'

    def __unicode__(self):
        return u'%s' % self.qualifications


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
