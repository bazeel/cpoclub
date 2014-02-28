from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import User


class InvitationCode(models.Model):
    code = models.CharField(_('invitation code'), primary_key=True, max_length=255)

    def __unicode__(self):
        return self.code

    class Meta:
        verbose_name = _('invitation code')
        verbose_name_plural = _('invitation codes')


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=_('user'), related_name='profile')
    invitation_code = models.OneToOneField(InvitationCode, verbose_name=_('invitation code'), related_name='profile')

    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profile')