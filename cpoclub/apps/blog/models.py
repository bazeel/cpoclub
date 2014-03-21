from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from tinymce import models as tinymce_models


class Record(models.Model):

    user = models.ForeignKey(User, verbose_name=_('user'), related_name='records') 
    active = models.BooleanField(_('active'), default=False)
    public = models.BooleanField(_('public'), default=False)
    title = models.CharField(_('title'), max_length=255)
    preview = models.TextField(_('preview'))
    content = tinymce_models.HTMLField(_('content'))
    date = models.DateField(_('date'),auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-date']
        verbose_name = _('record')
        verbose_name_plural = _('records')

    def __unicode__(self):
        return self.title

    def active_comments(self):
        comments = Comment.objects.filter(active=True, record__pk=self.pk)
        return comments

    @models.permalink
    def get_absolute_url(self):
        return ('record_detail', (), {'pk': self.pk})


class Comment(models.Model):

    user = models.ForeignKey(User, verbose_name=_('user'), related_name='comments')
    record = models.ForeignKey(Record, verbose_name=_('record'), related_name='comments')
    active = models.BooleanField(_('active'), default=False)
    comment = models.TextField(_('comment'))
    date = models.DateTimeField(_('date'), auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-date']
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def __unicode__(self):
        title = (self.comment[:75] + '...') if len(self.comment) > 75 else self.comment
        return title