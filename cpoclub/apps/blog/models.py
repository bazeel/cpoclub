from django.db import models
from django.utils.translation import ugettext_lazy as _

from tinymce import models as tinymce_models


class Record(models.Model):

    active = models.BooleanField(_('active'), default=True)
    public = models.BooleanField(_('public'), default=True)
    title = models.CharField(_('title'), max_length=255)
    preview = models.TextField(_('preview'))
    content = tinymce_models.HTMLField(_('content'))
    date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-date']
        verbose_name = _('record')
        verbose_name_plural = _('records')

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog_detail', (), {'pk': self.pk})
