from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    title = models.CharField(_('title'), max_length=255)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __unicode__(self):
        return self.title


class Doc(models.Model):
    category = models.ForeignKey(Category, verbose_name=_('category'), related_name='documents') 
    title = models.CharField(_('title'), max_length=255)
    active = models.BooleanField(_('active'), default=True)
    preview = models.TextField(_('preview'))
    file = models.FileField(_('file'), upload_to='library')

    class Meta:
        ordering = ['title']
        verbose_name = _('document')
        verbose_name_plural = _('documents')