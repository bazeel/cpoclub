from django.db import models
from django.utils.translation import ugettext_lazy as _

from tinymce import models as tinymce_models


class Event(models.Model):
    date = models.DateField(_('date'))
    city = models.CharField(_('city'), max_length=255)
    address = models.CharField(_('address'), max_length=255)
    coordinate = models.CharField(_('coordinate'), 
        help_text='<a target="_blank" href="http://api.yandex.ru/maps/tools/getlonglat/">http://api.yandex.ru/maps/tools/getlonglat/</a>',
        max_length=255)
    active = models.BooleanField(_('active'), default=True)
    preview = models.TextField(_('preview'), blank=True)
    content = tinymce_models.HTMLField(_('content'))


    class Meta:
        ordering = ['-date']
        verbose_name = _('event')
        verbose_name_plural = _('events')


class Image(models.Model):
    event = models.ForeignKey(Event, verbose_name=_('event'), related_name='images') 
    image = models.ImageField(_('image'), upload_to='events', blank=True)

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')