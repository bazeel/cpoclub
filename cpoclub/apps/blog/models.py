from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):

    language = models.CharField(_('language'), max_length=3, choices=settings.LANGUAGES)
    title = models.CharField(_('title'), max_length=255)
    preview = models.TextField(_('preview'))
    content = tinymce_models.HTMLField(_('content'))
    interesting = models.BooleanField(_('very interesting'))
    date = models.DateField(_('date'))

    class Meta:
        ordering = ['-date']
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog_detail', (), {'pk': self.pk})
