from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


EMPLOYEE_ROLES = (
    ('owner', 'Owner'),
    ('manager', 'Manager'),
    ('administrator', 'Administrator'),
    # ('teacher', 'Teacher'),
)


class UserProfile(models.Model):

    # objects = UserProfileManager()

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    user = models.OneToOneField(User, related_name='profile')

    wants_email = models.BooleanField(null=False, default=True)
    website = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    post_code = models.CharField(max_length=20, null=True, blank=True)

    def __unicode__(self):
        return 'UserProfile for %s' % self.user
