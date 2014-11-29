from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from pong.util.models import PongModel


class UserProfile(PongModel):

    # objects = UserProfileManager()

    user = models.OneToOneField(User, related_name='profile')

    wants_email = models.BooleanField(null=False, default=True)

    def __unicode__(self):
        return 'UserProfile for %s' % self.user
